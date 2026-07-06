# Candidate C03: Golden Boot vs. Champion Nation (Rank 1)

## Claim
Only 3 of 22 World Cup tournaments (13.6%) had the Golden Boot top scorer come from the champion nation — the prize-winning striker overwhelmingly plays for a team that does NOT win the tournament.

## Registered Prior (written BEFORE examining the data)
Prior: 30–40% expected. Rationale: the champion presumably has the strongest squad, so the best striker (capable of winning the Golden Boot) would often be on that team. If the champion wins ~5 goals/match collectively, a top striker on that team would naturally accumulate goals.

## Why It Would Be Surprising
The result of 13.6% is less than half the prior lower bound. This implies that "most goals scored" and "best team" are virtually uncorrelated — winning the World Cup appears to be a collective defensive-plus-organized-attack achievement, not dominated by an individual scoring machine.

## Evidence Feasibility
HIGH. Directly computed from piterfm/world_cup.csv (22 rows). Fields: Champion, TopScorrer. Confirmed 3 matches: 1978 Kempes (Argentina), 1982 Rossi (Italy), 2002 Ronaldo (Brazil). No data engineering required.

## Novelty Check
Novelty check unavailable (no web search). The individual cases (Kempes 1978, Rossi 1982, Ronaldo 2002) are known; the aggregated 13.6% statistic appears not to be a standard published figure.

## Dataset Reference
- piterfm/world_cup.csv: Year, Champion, TopScorrer (n=22 rows)
