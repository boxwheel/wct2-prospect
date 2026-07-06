# Candidate C01: Second-Half Goal Acceleration in the 76–90 Minute Window (Rank 3)

## Claim
Goals in the 76–90 minute window are ≥40% more frequent than goals in any single 15-minute window of the first half — the final quarter-hour of normal time is dramatically overrepresented in World Cup scoring.

## Registered Prior (written BEFORE examining the data)
Prior: a gradual increase in goals as the match progresses, driven by fatigue and desperation, with ~10–25% more goals in the 76–90 window than the first-half average. A linear or gently accelerating distribution.

## Why It Would Be Surprising
If the actual ratio is ≥40% (observed: 457 goals in 76–90 vs 303 in 31–45, the worst first-half window), it indicates a structural non-linearity — not just fatigue but a discrete late-game acceleration, possibly driven by accumulated yellow cards leading to bolder play, substitution patterns, and psychological pressure in knock-out contexts.

## Evidence Feasibility
HIGH. WorldCupPlayers.csv Event field encodes "G{minute}'" for all goals. Scouting parsed 2,194 goal-minute events from 1930–2014 (abecklas dataset). Distribution by 15-minute bins: 1–15: 294, 16–30: 324, 31–45: 303, 46–60: 354, 61–75: 398, 76–90: 457, 91+: 64. Chi-squared test for uniform distribution is straightforward.

## Novelty Check
Novelty check unavailable. General knowledge that late goals are more common is widely cited, but the specific 15-minute window breakdown from this dataset is not a standard published figure.

## Dataset Reference
- abecklas/WorldCupPlayers.csv: Event column, ~37,784 rows, 1930–2014
