# System Architecture

## Architecture Position

Kaikou Engine is designed as a local-first, cloud-ready pipeline.

```text
Platform Signals
-> Signal Collector
-> Normalizer
-> Cognitive Topic Extractor
-> Classifier
-> Model Mapper
-> Viral Scorer
-> Script Generator
-> Editing Generator
-> Subtitle Formatter
-> Publishing Packager
-> History Store
```

## Local Layer

The local layer handles:

- WorkBuddy-assisted collection
- local files
- local history database
- daily content generation
- exportable Markdown output

## Core Layer

The core layer must not depend on one collection method.

It receives normalized signal records and produces structured content packages.

## Cloud-Ready Layer

Future cloud modules may include:

- hosted task runner
- cloud database
- object storage for raw signals and outputs
- web dashboard
- scheduled pipeline runs
- collaboration and review workflow

## Module Boundary

Collection can change without rewriting generation.

Generation can change without rewriting storage.

Storage can move from local SQLite to cloud Postgres without changing the content rules.

