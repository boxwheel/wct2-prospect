# Candidate C14: Comeback Win Rate Is Higher in Knockout Rounds Than in Group Stage (Rank 5)

## Claim
Teams trailing at half-time win the full match (comeback) more often in knockout rounds than in group stage — the elimination stakes force more desperate attacking play, reversing the naive "safe draw" hypothesis.

## Registered Prior (written BEFORE examining the data)
Prior: group-stage comeback rate > knockout-stage rate. Rationale: in group stage, a trailing team knows a draw still earns a point and may qualify them; the urgency to score is lower. In knockout stage, a draw sends the game to extra time — the trailing team has existential pressure. I expect knockout comebacks to be higher (5–10 percentage points above group stage).

## Why It Would Be Surprising
If the expected direction holds (knockout > group), it confirms "elimination pressure increases comebacks." If group > knockout, it reveals that trailing teams in knock-out games play MORE defensively (protect the draw, go to extra time) rather than chasing wins — a psychologically counter-intuitive finding. Either direction cleanly falsifies the other prior.

## Evidence Feasibility
HIGH. abecklas/WorldCupMatches.csv has Half-time Home Goals, Half-time Away Goals, final goals, and Stage (1930–2014). Identify matches where HT loser reversed to win (comeback), split by stage type. For 2018/2022, piterfm has round labels and full-time scores (no HT data).

## Novelty Check
Novelty check unavailable. Comeback rates within football tournaments are studied generally, but the specific group/knockout comparison using half-time data from this dataset appears novel.

## Dataset Reference
- abecklas/WorldCupMatches.csv: Half-time goals + final goals + Stage (n=852 rows, 1930–2014)
