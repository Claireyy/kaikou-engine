# Cloud Migration Plan

## Local-First Baseline

Version 0.1 runs locally:

- raw signals in local files
- outputs in local files
- history in local storage
- WorkBuddy for browser-side automation

## Migration Candidates

### Storage

Local:

- `data/raw_signals/`
- `outputs/`
- SQLite history database

Cloud-ready replacement:

- object storage for raw signals and generated output
- Postgres or Supabase for history and metadata

### Pipeline Runtime

Local:

- Python scripts

Cloud-ready replacement:

- scheduled jobs
- FastAPI service
- serverless function
- queue-based worker

### Interface

Local:

- command line
- Markdown output

Cloud-ready replacement:

- web dashboard
- review queue
- publish calendar

## Design Constraint

The core engine must accept normalized input and return structured output. It should not know whether data came from WorkBuddy, manual files, or a cloud collector.

