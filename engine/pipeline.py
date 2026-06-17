"""Pipeline orchestration entrypoint."""

from __future__ import annotations

from pathlib import Path

from engine.dedup import deduplicate_topics
from engine.generator import generate_packages
from engine.models import ContentPackage, TopicCandidate
from engine.normalizer import normalize_signals, select_top_topics
from engine.storage import load_raw_signals, write_run_output


def run_pipeline(input_path: Path, output_dir: Path, output_count: int = 4) -> list[ContentPackage]:
    signals = load_raw_signals(input_path)
    candidates = normalize_signals(signals)
    unique_candidates = deduplicate_topics(candidates)
    topics = select_top_topics(unique_candidates, limit=output_count)
    packages = generate_packages(topics)
    write_run_output(output_dir, topics, packages)
    return packages


def preview_topics(input_path: Path, output_count: int = 4) -> list[TopicCandidate]:
    signals = load_raw_signals(input_path)
    candidates = deduplicate_topics(normalize_signals(signals))
    return select_top_topics(candidates, limit=output_count)
