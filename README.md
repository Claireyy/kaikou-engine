# Kaikou Engine

Kaikou Engine is a local-first cognitive short-video content pipeline.

It converts internet attention signals into four complete short-video content packages per run:

- cognitive topic
- one-minute spoken script
- editing structure
- subtitle-ready text
- publishing captions and hashtags

The project is designed to run locally first and migrate selected modules to cloud infrastructure later.

## Current Scope

Version 0.1 focuses on a manual or semi-automated input workflow:

1. Collect platform signals into `data/raw_signals/`.
2. Normalize signals into a shared schema.
3. Extract and score cognitive topics.
4. Generate four complete video packages.
5. Store output and history for deduplication.

## Design Principles

- Local-first, cloud-ready.
- Public-repo safe by default.
- Platform collection is separate from the content engine.
- Prompts are versioned as project assets.
- Every run produces exactly four content packages.

## Repository Layout

See `docs/system_architecture.md` for the planned structure and module boundaries.

