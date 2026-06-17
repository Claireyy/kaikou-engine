# Kaikou Engine

Kaikou Engine is a local-first cognitive short-video content pipeline.

It converts internet attention signals into four complete short-video content packages per run:

- cognitive topic
- one-minute spoken script
- editing structure
- subtitle-ready text
- publishing captions and hashtags

The project is designed to run locally first and migrate selected modules to cloud infrastructure later.

## Repository Strategy

This repository is intended to be public-safe.

It should contain:

- project structure
- public architecture notes
- non-sensitive prompt templates
- abstract pipeline logic
- sample schemas

It should not contain:

- real platform cookies or tokens
- WorkBuddy private automation profiles
- unpublished scripts
- raw platform data
- private prompt assets
- production cloud credentials

Private assets should live outside this repository or in a separate private repository.

## Current Scope

Version 0.1 focuses on a manual or semi-automated input workflow:

1. Collect platform signals into `data/raw_signals/`.
2. Normalize signals into a shared schema.
3. Extract and score cognitive topics.
4. Generate four complete video packages.
5. Store output and history for deduplication.

## Local Run

Run the sample pipeline:

```bash
python3 scripts/run_daily_pipeline.py --input data/samples/sample_signals.json --output outputs/daily_runs/sample_run
```

Run tests with the Python standard library:

```bash
python3 -m unittest discover -s tests
```

## Daily Closed Loop

For real daily operation, see:

- `docs/daily_operation.md`
- `integrations/workbuddy/kaikou_signal_collector_skill.md`

The daily flow is:

1. WorkBuddy or manual collection writes `data/raw_signals/today.json`.
2. Validate the input.
3. Run the pipeline.
4. Review `outputs/daily_runs/<timestamp>/full_package.md`.
5. Local history is appended to `data/history/history.jsonl`.

To paste into Kaikou, use:

```bash
python3 scripts/copy_kaikou_editor_text.py outputs/daily_runs/<timestamp>
```

To create a Kaikou task link:

```bash
python3 scripts/create_kaikou_link.py outputs/daily_runs/<timestamp> --copy
```

Script-writing rules for short spoken lines are documented in:

- `integrations/workbuddy/kaikou_script_writer_skill.md`

The v4.0 content system specification is documented in:

- `docs/v4_content_system.md`

## Design Principles

- Local-first, cloud-ready.
- Public-repo safe by default.
- Platform collection is separate from the content engine.
- Prompts are versioned as project assets.
- Every run produces exactly four content packages.

## Repository Layout

See `docs/system_architecture.md` for the planned structure and module boundaries.
