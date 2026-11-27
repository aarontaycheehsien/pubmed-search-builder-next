#!/usr/bin/env python3
"""Idea 6 with the weak qualifier and the known-record guard together (development topics only).

Run from evals/experiments: python idea6_weak_guard.py. Prints pooled totals and per-topic losses and refusals."""
sys.path.insert(0,'.'); sys.path.insert(0,'..'); sys.path.insert(0,'../../scripts')
import harness, replay
import idea6_robustness as R
from ideas_126 import Lab
from ideas_6b_2b import DATE_TERM, QUALIFIERS, cards_for
tot=dict(lost=0,unseen=0,refused=0,kept=0.0,count=0,strat=0,losing=0); per={}
for topic in harness.load_splits()["dev"]:
    q,seen=QUALIFIERS[topic]; wq=R.weak(q)
    f=harness.load_fixture(topic); lab=Lab(f)
    gold=sorted(lab.among("",[str(p) for p in f["gold_pmids"]])); rng=random.Random(R.SEED)
    known=set(rng.sample(gold,max(3,round(R.KNOWN_SHARE*len(gold)))))
    for label,card in cards_for(topic):
        try: blocks=[b["terms"] for b in replay.blocks_of(card["strategy"])]
        except SystemExit: continue
        dq=R.query(blocks); base=lab.among(dq,gold); bc=lab.count(dq)
        imp=[]
        for bi,b in enumerate(blocks):
            for ti,t in enumerate(b):
                if DATE_TERM.search(t) or len(b)==1: continue
                w=[list(x) for x in blocks]; w[bi]=[x for j,x in enumerate(b) if j!=ti]
                imp.append((lab.count(f"({dq}) NOT ({R.query(w)})"),bi,ti,t))
        imp.sort(reverse=True); acc=[]; ref=0
        for it in imp[:5]:
            trial=R.restructure(blocks,acc+[it],wq)
            if (known&base)-lab.among(R.query(trial),known&base): ref+=1; continue
            acc.append(it)
        fin=R.query(R.restructure(blocks,acc,wq)); hit=lab.among(fin,gold); lost=base-hit
        tot['lost']+=len(lost); tot['unseen']+=len(lost-known); tot['refused']+=ref; tot['kept']+=lab.count(fin); tot['count']+=bc; tot['strat']+=1; tot['losing']+=bool(lost)
        p=per.setdefault(topic,[0,0]); p[0]+=len(lost); p[1]+=ref
print(json.dumps({**tot,'kept_pooled':round(tot['kept']/tot['count'],3)})); print({k:v for k,v in per.items() if v[0] or v[1]})
