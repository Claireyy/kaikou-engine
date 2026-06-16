# Workflow

## Version 0.1 Workflow

1. Collect platform observations.
2. Save raw signals into `data/raw_signals/`.
3. Normalize all signals into a shared schema.
4. Extract candidate cognitive topics.
5. Score each topic.
6. Keep the top four topics.
7. Generate four complete video packages.
8. Save outputs into `outputs/daily_runs/`.
9. Write topic and script metadata into history.

## Standard Run Output

Each run must generate:

- `00_topic_scores.md`
- `01_package.md`
- `02_package.md`
- `03_package.md`
- `04_package.md`
- `full_package.md`

