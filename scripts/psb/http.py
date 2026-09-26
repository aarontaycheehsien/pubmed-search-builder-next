"""Small standard-library HTTP transport with retries, pacing, and secret redaction."""

from __future__ import annotations

import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Callable, Mapping

TRANSIENT_STATUS = frozenset({408, 429, 500, 502, 503, 504})
SECRET_PARAMS = frozenset({"api_key", "apikey", "token", "access_token", "authorization"})


class TransportError(RuntimeError):
    def __init__(self, message: str, *, transient: bool) -> None:
        super().__init__(message)
        self.transient = transient


@dataclass(frozen=True)
class Policy:
    retries: int = 3
    backoff_seconds: float = 1.0
    timeout_seconds: float = 30.0
    per_second: float = 0.0


def redact_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    pairs = [
        (key, "***" if key.casefold() in SECRET_PARAMS else value)
        for key, value in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    ]
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(pairs)))


class Transport:
    """urllib transport. The opener, clock and sleeper are injectable for tests."""

    def __init__(
        self,
        *,
        opener: Callable | None = None,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._open = opener or urllib.request.urlopen
        self._clock = clock
        self._sleep = sleep
        self._next_allowed = 0.0

    def request(
        self,
        url: str,
        params: Mapping[str, str],
        *,
        method: str = "GET",
        headers: Mapping[str, str] | None = None,
        policy: Policy = Policy(),
    ) -> bytes:
        encoded = urllib.parse.urlencode(dict(params))
        if method == "POST":
            request = urllib.request.Request(url, data=encoded.encode("utf-8"), method="POST")
        else:
            request = urllib.request.Request(f"{url}?{encoded}" if encoded else url, method="GET")
        for name, value in (headers or {}).items():
            request.add_header(name, value)

        for attempt in range(policy.retries + 1):
            if policy.per_second > 0:
                wait = self._next_allowed - self._clock()
                if wait > 0:
                    self._sleep(wait)
            try:
                with self._open(request, timeout=policy.timeout_seconds) as response:
                    body = response.read()
                if policy.per_second > 0:
                    self._next_allowed = self._clock() + 1.0 / policy.per_second
                return body
            except urllib.error.HTTPError as exc:
                transient = exc.code in TRANSIENT_STATUS
                detail = exc.read().decode("utf-8", errors="replace")[:300]
                message = f"HTTP {exc.code} for {redact_url(request.full_url)}: {detail}"
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                transient = True
                message = f"request failed for {redact_url(request.full_url)}: {exc}"
            if not transient or attempt >= policy.retries:
                raise TransportError(message, transient=transient)
            self._sleep(policy.backoff_seconds * (2**attempt))
        raise AssertionError("unreachable")
