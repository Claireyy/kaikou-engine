# Daily Operation

## Goal

Run one local content cycle and produce four complete short-video packages.

## Step 1: Collect Signals

Create a raw signal file from the public template:

```text
data/raw_signals/input_template.json
```

For real daily work, save the filled file as:

```text
data/raw_signals/today.json
```

The real `today.json` file is ignored by Git.

## Step 2: Validate Input

```bash
python3 scripts/validate_input.py data/raw_signals/today.json
```

Fix validation errors before generating content.

## Step 3: Generate Four Packages

```bash
python3 scripts/run_daily_pipeline.py --input data/raw_signals/today.json
```

The output is written to:

```text
outputs/daily_runs/<timestamp>/
```

Each run contains:

- `00_topic_scores.md`
- `01_package.md`
- `02_package.md`
- `03_package.md`
- `04_package.md`
- `full_package.md`
- `kaikou_paste.md`
- `run.json`

## Step 4: Review and Use

Open `full_package.md`, then select the four scripts for filming, editing, and publishing.

If you want to paste the result into Kaikou, open `kaikou_paste.md`.

Direct publishing or short-link generation will be added after the Kaikou site exposes a URL, API, or upload format.

On macOS, copy only the Kaikou editor-ready script text directly to the clipboard:

```bash
python3 scripts/copy_kaikou_editor_text.py outputs/daily_runs/<timestamp>
```

Then paste it into the Kaikou `文案` box and click `生成短链接`.

Create a Kaikou task link:

```bash
python3 scripts/create_kaikou_link.py outputs/daily_runs/<timestamp> --copy
```

If the short-link API is unavailable, the script writes a fallback long link that still opens the task package in Kaikou.

## Step 5: History

The pipeline appends selected topic metadata to:

```text
data/history/history.jsonl
```

This file is local-only and ignored by Git.
