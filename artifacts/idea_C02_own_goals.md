# Candidate C02: Own Goal Asymmetry (Rank 2)

## Claim
Home teams (listed first in World Cup match records) score own goals at 2.29× the rate of away teams across all 964 matches (1930–2022): 39 home own goals vs 17 away own goals.

## Registered Prior (written BEFORE examining the data)
Prior: roughly equal rates, or a slight away-team advantage (1.0–1.3:1 ratio). Rationale: away teams tend to defend their own goal more heavily (playing deeper), so they have more opportunities to deflect shots into their own net. One might expect away-team own goal rate to be slightly higher, not lower.

## Why It Would Be Surprising
A 2.29:1 ratio far exceeds the prior. If real, it suggests the "home" listing in World Cup records systematically captures one team's attacking posture — home teams push forward more, leave defenders exposed to cross-into-own-goal scenarios. The counterintuitive direction (attacking teams score more own goals) demands an explanation.

## Evidence Feasibility
HIGH. Directly computed from piterfm/matches_1930_2022.csv, columns home_own_goal and away_own_goal. String presence check required (notna + non-empty). n=56 own goals total: 39 home, 17 away. Feasible chi-squared test with p-value.

## Novelty Check
Novelty check unavailable. This specific 2.29:1 asymmetry does not appear in standard football statistics publications (it would require the specific Kaggle dataset analysis to surface).

## Dataset Reference
- piterfm/matches_1930_2022.csv: home_own_goal, away_own_goal (n=964 rows)
