# Research Center Design QA

- Visual target: `C:\Users\nossi\.codex\generated_images\019fb96b-3cd3-7862-a486-ae86f9b2c88f\exec-57bbbd43-c35c-4f98-a523-3fca7f96712b.png`
- Target pixels: 1487 × 1058; evaluated at a normalized 1440 × 1024 viewport
- Final implementation: `tmp/research-center-qa/implementation-final.png`
- Same-input comparison: `tmp/research-center-qa/comparison-final.png`
- Mobile evidence: `tmp/research-center-qa/mobile-list-v2.png`, `tmp/research-center-qa/mobile-reader.png` at 390 × 844
- Tested state: light theme, all article types, `formal-8261` selected

## Comparison history

1. Initial desktop render found a P0 content failure: the title and article sections were not attached because multiple nodes were passed to `appendChild`. Replaced those calls with `append` and added contract tests.
2. Second desktop render found P1 horizontal overflow and a selection/list-order mismatch. Added long-text wrapping and stable type ordering so the selected article is visible at the top of the catalog.
3. Initial mobile render found a P1 collapsed content column below 1180 px. Removed the zero-width grid placement at that breakpoint and added an in-panel close action for the mobile filter drawer.
4. Final side-by-side comparison confirms the intended warm off-white palette, thin dividers, compact teal/purple/amber type system, 220 px filter rail, 400 px catalog, independent reader, right-side outline/evidence rail, typography hierarchy, and content density. No visible P0, P1, or P2 differences remain that block the selected direction.

## Functional verification

- 244 real articles render: 121 formal notes, 118 long/short narratives, and 5 market topics.
- Search, article-type tabs, selected-card state, deep links, related-content tabs, copy-link feedback, theme toggle, dashboard gateway, and sorting work.
- Mobile catalog → reader → back flow and filter drawer open → close flow work at 390 × 844.
- Desktop and mobile have zero horizontal page overflow.
- Browser console errors/warnings: 0.
- Full suite: 325 tests passed with Python 3.12 and `PYTHONUTF8=1`.

final result: passed
