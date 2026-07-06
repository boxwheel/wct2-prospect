# wct2-prospect

**Layer-2 Prospect** for the `wct2` Flywheel campaign: "Surprising Facts about the FIFA World Cup (1930–2022)".

## What this repo contains

- `src/scout.py` — Data scouting script that explores both Kaggle datasets for hypothesis feasibility
- `artifacts/feasibility_stats.json` — Machine-readable scouting output (key counts, distributions)
- `artifacts/slate_candidates.md` — Full 25-candidate hypothesis table with registered priors, feasibility, novelty checks, and screening decisions

## Role

This is the **generation-only** layer. No experiments are run here. The gate layer picks 2–4 survivors from the 8 shortlisted candidates for experiment execution boxes.

## Data sources

- `kaggle datasets download abecklas/fifa-world-cup`
- `kaggle datasets download piterfm/fifa-football-world-cup`

## Reproducing the scouting

```bash
pip install pandas numpy kaggle
kaggle datasets download abecklas/fifa-world-cup -p ./data/abecklas --unzip
kaggle datasets download piterfm/fifa-football-world-cup -p ./data/piterfm --unzip
python3 src/scout.py
```
