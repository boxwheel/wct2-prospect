# Candidate C09: First-Goal Win Rate Diverges Between Group Stage and Knockout Rounds (Rank 4)

## Claim
Teams that score first in a World Cup match win ≥75% overall; but this win rate differs significantly between group stage (where a draw may still be tactically acceptable) and knockout stage (where a draw leads to extra time) — the direction of divergence is the uncertain element.

## Registered Prior (written BEFORE examining the data)
Prior: first-goal teams win 70–75% overall (near baseline expectation). In knockout stage, expect this to be slightly higher (≥80%) because the threat of extra time deters trailing teams from taking risks that might lead to a counter-goal. In group stage, expect slightly lower (60–70%) because teams may settle for a draw once ahead.

## Why It Would Be Surprising
If the knockout first-goal win rate is LOWER than group stage, it would invert the prediction: elimination pressure makes teams attack harder when trailing, leading to more comebacks in knockouts. Alternatively, if group-stage first-goal win rate exceeds 80%, it suggests groups are more dominated by early goals than knockouts — also surprising.

## Evidence Feasibility
HIGH. Requires joining WorldCupPlayers.csv (first goal event by MatchID) with WorldCupMatches.csv (stage, final score). Both have MatchID. The Stage field in abecklas covers 1930–2014; piterfm's Round field covers 1930–2022. A first-goal lookup per match is feasible.

## Novelty Check
Novelty check unavailable. First-goal win rates in football are widely studied, but the specific group/knockout breakdown across all World Cups (1930–2022) appears novel.

## Dataset Reference
- abecklas/WorldCupPlayers.csv + WorldCupMatches.csv (MatchID join)
- piterfm/matches_1930_2022.csv: Round + home_goal / away_goal columns
