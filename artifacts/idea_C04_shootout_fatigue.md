# Candidate C04: Teams That Won via Penalty Shootout Lose Their Next Knockout Match at ≥30% Higher Rate Than Baseline (Rank 7)

## Claim
Teams that advanced via penalty shootout face a measurably elevated loss rate in their very next knockout match — the physical and psychological toll of a shootout imposes a structural disadvantage beyond normal fatigue.

## Registered Prior (written BEFORE examining the data)
Prior: 10–15% higher loss rate than baseline expected. Baseline loss rate in knockout rounds (excluding finals) is roughly 50% (since one team must lose each knockout match). A 10–15% higher rate (i.e., 55–65% loss rate) seems plausible from fatigue.

## Why It Would Be Surprising
If the post-shootout loss rate exceeds 65% (≥30% above baseline), it suggests a more profound structural effect — psychological "hangover," depleted substitutes, or accumulated yellow cards from extra time materially handicap the next match at a rate greater than simple fatigue models predict.

## Evidence Feasibility
HIGH. piterfm has Notes field (35 shootout matches), dates (all 964 matches), and full-time scores. Can identify each shootout winner, find their next match, and compute loss rate vs. the baseline knockout loss rate. n=35 is moderate; confidence interval required.

## Novelty Check
Novelty check unavailable. Post-shootout fatigue is discussed anecdotally in sports media, but the specific quantified statistic (% higher loss rate in the following match) from this complete dataset appears novel.

## Dataset Reference
- piterfm/matches_1930_2022.csv: Notes, Date, Round, home_team, away_team, home_score, away_score (n=964 rows)
