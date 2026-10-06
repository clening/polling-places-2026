# Polling places in scope for selected 2026 Senate and House races

A ballpark count of Election Day polling places covering a specific set of 2026 races, built from the EAC's 2024 Election Administration and Voting Survey (EAVS).

## Result

| Scope | Senate states | House-only districts | Total |
|---|---|---|---|
| Senate states in full | 26,479 | ~4,600 | ~31,100 |
| Counties within 30 points | 16,404 | ~4,600 | ~21,000 |
| Counties within 20 points | 11,282 | ~4,600 | ~15,900 |
| Counties within 10 points | 5,537 | ~4,600 | ~10,100 |

"Within N points" keeps only counties whose 2024 presidential margin was N points or less in either direction, as a proxy for contested areas.

## Races covered

- **Senate (statewide):** TX, IA, AK, OH, KS, MI, NC, GA, NH, FL, SC.
- **House, outside those states:** AL-2, KY-6, LA-6, ME-2, MT-1, NE-2, NJ-7, NY-17, PA-1, PA-7, PA-8, PA-10, TN-9, VA-1, VA-2, WI-1, WI-3.
- **Dropped as mostly vote-by-mail or early voting:** districts in AZ, CA, CO, UT and WA.
- House districts inside the Senate states are not counted separately, since the statewide count already covers them.

## Files

- `calc.py`: Senate-state bands and House-only district totals.
- `calc_wi.py`: WI-1 and WI-3. Wisconsin reports by municipality, so `calc.py` prints 0 for these; use this script's figures.
- `2024_EAVS_for_Public_Release_nolabel_V2.csv`: EAVS 2024 jurisdiction-level data. Polling places are question `D3a`.
- `eavs2024.pdf`: the EAVS 2024 Comprehensive Report (state totals are in Appendix A, Overview Table 3).
- `pres24.csv`: 2024 presidential results by county.

Run the scripts from this folder with `python3 calc.py` and `python3 calc_wi.py`. They need only the standard library.

## Caveats

- This is a rough estimate, not an authoritative count.
- Counties were assigned to House districts by hand, with rough fractions for split counties. Districts redrawn since 2024 may not match.
- LA-6 (~325) and TN-9 (~195) are not in the scripts. They are the state total divided by the number of districts.
- Listed House districts inside Senate states are not added back when their counties fall outside the margin band, so the narrowed totals are slightly low.
- About 300 Wisconsin polling places are in municipalities spanning several counties and are not assigned.
- Early voting sites are excluded.

## Sources

- EAVS 2024 data and report: U.S. Election Assistance Commission, <https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys>
- County presidential results: <https://github.com/tonmcg/US_County_Level_Election_Results_08-24> (MIT licence)
