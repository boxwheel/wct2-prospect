# Candidate C13: Half-Time Score Margin Predicts Comeback Probability Non-Linearly — 2-Goal HT Deficit Is Near-Certain Loss (Rank 6)

## Claim
Teams trailing by exactly 1 goal at half-time win the match (comeback) in approximately 8–12% of cases; but teams trailing by 2 goals at half-time win in fewer than 2% of cases — the drop from 1-goal to 2-goal HT deficit is far larger than linear scaling would predict.

## Registered Prior (written BEFORE examining the data)
Prior: expect non-linearity, but estimate ~5% for 2-goal HT deficits (roughly 40% of the 1-goal rate, not 80%). The precise rate is unknown; the foundation baseline gives 8.2% overall reversal rate for all HT trailers combined.

## Why It Would Be Surprising
If the 2-goal deficit comeback rate is <2% (less than a quarter of the 1-goal rate), it reveals a near-deterministic effect: a 2-goal HT lead is essentially a closed game. The non-linearity would have tactical implications (teams should switch strategy completely at -2 vs -1).

## Evidence Feasibility
HIGH. abecklas/WorldCupMatches.csv has Half-time Home Goals, Half-time Away Goals, final goals for 852 matches. Filter by HT deficit of exactly -1 vs -2 and compute win rate. Small n for -2 deficits (~50–80 matches estimated), so confidence interval must be reported.

## Novelty Check
Novelty check unavailable. The foundation already reports the 8.2% overall reversal rate; the per-margin breakdown (1-goal vs 2-goal deficits) is a genuine deepening of that finding and is not a standard published figure.

## Dataset Reference
- abecklas/WorldCupMatches.csv: Half-time Home Goals, Half-time Away Goals, Home Team Goals, Away Team Goals (n=852 rows)
