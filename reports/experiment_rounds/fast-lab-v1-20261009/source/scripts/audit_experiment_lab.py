#!/usr/bin/env python3
"""Independent return/rank/HAC recomputation of every lab candidate and horizon.

Uses the lab's signal builder (whose BASE is checked against the formal scorer),
but does NOT use its outcome, grouping, aggregation, uncertainty, or selection
helpers. This is numerical cross-checking, not independent alpha confirmation.
"""
import argparse
from collections import defaultdict
from contextlib import closing
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import statistics as st
import sys

import db_ro
import experiment_lab as lab


def rank(values):
    return [1 + sum(x < v for x in values) + (sum(x == v for x in values)-1)/2 for v in values]


def rho(x, y):
    a, b = rank(x), rank(y)
    ea, eb = [v-st.mean(a) for v in a], [v-st.mean(b) for v in b]
    norm = math.sqrt(sum(v*v for v in ea)*sum(v*v for v in eb))
    return sum(u*v for u,v in zip(ea,eb))/norm if norm else None


def quadratic_se(series, horizon, calendar):
    if len(series)/horizon < 3:
        return None
    positions = {d:i for i,d in enumerate(calendar)}
    mean = st.mean(series.values())
    variance = sum((a-mean)*(b-mean)*max(0,1-abs(positions[x]-positions[y])/horizon)
                   for x,a in series.items() for y,b in series.items())
    return math.sqrt(max(0,variance))/len(series)


def audit(con, report):
    cfg = report["config"]
    calendar, rows, frozen, _, _, _ = lab.load_inputs(con, report['as_of'])
    prices = {(r[0],r[1]):r[2] for r in con.execute("""SELECT p.date,p.stock_id,p.open*a.close/p.close
        FROM price p JOIN price_adj a USING(date,stock_id)
        WHERE p.open>0 AND p.close>0 AND a.close>0 AND p.date<=?""", (report['as_of'],))}
    sources = {"replay": lab.build_signals(rows,cfg,calendar)[0],
               "frozen_replay": lab.build_signals(frozen,cfg,calendar)[0]}
    sources["forward"] = sources["frozen_replay"]
    comparisons, max_error, series_count = 0, 0.0, 0

    def check(actual, expected, label):
        nonlocal comparisons, max_error
        comparisons += 1
        if actual is None or expected is None:
            if actual is not expected:
                raise AssertionError((label,actual,expected))
            return
        difference=abs(actual-expected)
        max_error=max(max_error,difference)
        if difference>1e-10:
            raise AssertionError((label,actual,expected))

    for dataset, data in report["datasets"].items():
        allowed=set(data['eligible_signal_dates'])
        structural={c:defaultdict(dict) for c in data['structure']}
        old={}
        for index,day in enumerate(calendar):
            if day not in allowed or day not in sources[dataset]:
                continue
            grouped={c:defaultdict(list) for c in structural}
            for group,stocks in sources[dataset][day].items():
                names=sorted(stocks)
                if len(names)<cfg['min_group']:
                    continue
                base_values=[stocks[s]['BASE'] for s in names]
                base_top={s for s,r in zip(names,rank(base_values)) if (r-1)/(len(names)-1)>=.75}
                for candidate in structural:
                    values=[stocks[s][candidate] for s in names]
                    top={s for s,r in zip(names,rank(values)) if (r-1)/(len(names)-1)>=.75}
                    grouped[candidate]['tie_fraction'].append(1-len(set(values))/len(values))
                    if top and base_top:
                        grouped[candidate]['top_jaccard'].append(len(top & base_top)/len(top | base_top))
                    previous=old.get((candidate,group))
                    if previous and previous[0]+1==index and top and previous[1]:
                        grouped[candidate]['list_change'].append(1-len(top & previous[1])/len(top | previous[1]))
                    old[candidate,group]=(index,top)
            for candidate, metrics in grouped.items():
                for metric, values in metrics.items():
                    structural[candidate][metric][day]=st.mean(values)
        for candidate,result in data['structure'].items():
            for metric in ('tie_fraction','top_jaccard','list_change'):
                expected=structural[candidate][metric]
                actual=result['daily'].get(metric,{})
                if set(expected)!=set(actual):
                    raise AssertionError(f'{dataset}/{candidate}/{metric}: structural dates differ')
                for day,value in expected.items():
                    check(actual[day],value,'structural daily')
                if expected:
                    summary=result['summary'][metric]
                    check(summary['mean'],st.mean(expected.values()),'structural mean')
                    check(summary['se'],quadratic_se(expected,1,calendar),'structural HAC')
                    series_count+=1
        for h, candidates in data['horizons'].items():
            horizon=int(h)
            independent={c:defaultdict(dict) for c in candidates}
            for index,day in enumerate(calendar):
                if day not in allowed or day not in sources[dataset] or index+horizon+1>=len(calendar):
                    continue
                by_metric={c:defaultdict(list) for c in candidates}
                for stocks in sources[dataset][day].values():
                    names=sorted(stocks)
                    if len(names)<cfg['min_group']:
                        continue
                    entry,exit_day=calendar[index+1],calendar[index+1+horizon]
                    if any((entry,s) not in prices or (exit_day,s) not in prices for s in names):
                        continue
                    future=[prices[exit_day,s]/prices[entry,s]-1 for s in names]
                    base=[stocks[s]['BASE'] for s in names]
                    base_ic=rho(base,future)
                    for candidate in candidates:
                        values=[stocks[s][candidate] for s in names]
                        candidate_ic=rho(values,future)
                        if candidate_ic is None or base_ic is None:
                            continue
                        metrics={'ic':candidate_ic,'base_ic':base_ic,'delta_ic':candidate_ic-base_ic}
                        ranks=rank(values)
                        top=[i for i,v in enumerate(ranks) if (v-1)/(len(names)-1)>=.75]
                        bottom=[i for i,v in enumerate(ranks) if (v-1)/(len(names)-1)<=.25]
                        if top and bottom:
                            metrics['spread_pp']=100*(st.mean(future[i] for i in top)-st.mean(future[i] for i in bottom))
                            metrics['top_excess_gross_pp']=100*(st.mean(future[i] for i in top)-st.mean(future))
                            metrics['top_excess_cost_pp']=metrics['top_excess_gross_pp']-cfg['cost_pp']
                        for metric,value in metrics.items():
                            by_metric[candidate][metric].append(value)
                for candidate, metrics in by_metric.items():
                    for metric, values in metrics.items():
                        independent[candidate][metric][day]=st.mean(values)
            for candidate, result in candidates.items():
                for metric in ('ic','base_ic','delta_ic','spread_pp','top_excess_gross_pp','top_excess_cost_pp'):
                    expected=independent[candidate][metric]
                    actual=result['daily'].get(metric,{})
                    if set(expected)!=set(actual):
                        raise AssertionError(f'{dataset}/{h}/{candidate}/{metric}: dates differ')
                    for day,value in expected.items():
                        check(actual[day],value,f'{dataset}/{h}/{candidate}/{metric}/{day}')
                    if not expected:
                        continue
                    summary=result['summary'][metric]
                    check(summary['mean'],st.mean(expected.values()),'mean')
                    check(summary['se'],quadratic_se(expected,horizon,calendar),'HAC')
                    check(summary['n_days'],len(expected),'n')
                    check(summary['eff_obs'],len(expected)/horizon,'n/F')
                    position={d:i for i,d in enumerate(calendar)}
                    ordered=sorted(expected)
                    segments=1+sum(position[b]-position[a]!=1 for a,b in zip(ordered,ordered[1:]))
                    check(summary['episodes'],segments,'episodes')
                    series_count+=1
    return {'ok':True,'comparisons':comparisons,'series':series_count,'max_absolute_error':max_error,
            'scope':'Independent next-open returns, midranks, paired daily means, cohort spreads/cost, structural lists, calendar HAC; shared signal builder',
            'db_query_only':con.execute('PRAGMA query_only').fetchone()[0]}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--db',type=Path,default=lab.ROOT/'data/findmind.db')
    ap.add_argument('--report',type=Path,default=lab.ROOT/'reports/experiment_lab.json')
    ap.add_argument('--out',type=Path,default=lab.ROOT/'reports/experiment_lab_acceptance.json')
    args=ap.parse_args()
    protected = [args.db.resolve(), args.report.resolve()]
    if args.out.resolve() in protected or any((lab.ROOT/n).resolve() in args.out.resolve().parents for n in ('data','archive','config','scripts')):
        ap.error('output must not overwrite inputs or protected files')
    before=hashlib.sha256(args.db.read_bytes()).hexdigest()
    report=json.loads(args.report.read_text(encoding='utf-8'))
    if report['db_sha256']!=before or report['fingerprint']!=lab.check_registration(report['config']):
        raise ValueError('report/database/registered source mismatch')
    with closing(db_ro.connect(args.db)) as con:
        result=audit(con,report)
    if hashlib.sha256(args.db.read_bytes()).hexdigest()!=before:
        raise RuntimeError('database changed during audit')
    result.update(db_sha256=before,report_sha256=hashlib.sha256(args.report.read_bytes()).hexdigest(),
                  audit_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python=sys.version,platform=platform.platform(),utf8_mode=sys.flags.utf8_mode,
                  PYTHONUTF8=os.environ.get('PYTHONUTF8'),PYTHONIOENCODING=os.environ.get('PYTHONIOENCODING'))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(lab.canonical(result))
    print(json.dumps(result,ensure_ascii=True))


if __name__=='__main__':
    main()
