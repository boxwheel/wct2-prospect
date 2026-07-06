# Candidate C22: World Cup Finals Are the Lowest-Scoring Knockout Round — Fewer Goals Per Match Than QF, SF, or Third-Place Match (Rank 8)

## Claim
The championship final is, on average, the least-scoring match of any knockout round in the World Cup — below the average for quarterfinals, semifinals, and even the third-place match — making it quantifiably the most defensive game of the tournament.

## Registered Prior (written BEFORE examining the data)
Prior: finals probably average fewer goals than other knockout rounds, by maybe 0.3–0.5 goals per match. Estimated ranking (goals): Third-place match > QF > SF > Final. The specific values are unknown; prior is that the direction holds but the magnitude is modest.

## Why It Would Be Surprising
If the finding CONFIRMS the prior, it is honest confirmation, not discovery (SURPRISING:fail). However, if the third-place match significantly exceeds the final in goals (since there is nothing to lose in the third-place match and teams play more openly), the magnitude might be surprising. Alternatively, if QF averages higher than SF, which averages higher than Final, it reveals a monotonic tightening-of-defense as the stakes increase.

## Evidence Feasibility
HIGH. piterfm/matches_1930_2022.csv has Round and home_score + away_score for all 964 matches. Filtering by Round = 'Final', 'Semi-finals', 'Quarter-finals', 'Third-place match' is straightforward. n: ~22 finals, ~38 SFs, ~70 QFs, ~20 third-place matches.

## Novelty Check
Novelty check unavailable. The "finals are defensive" narrative is common, but the specific ranking of all four knockout rounds by goals-per-match using this complete dataset appears not to be a standard published figure.

## Dataset Reference
- piterfm/matches_1930_2022.csv: Round, home_score, away_score (n=964 rows)
