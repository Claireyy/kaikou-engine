"""Local and future cloud storage interfaces."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from engine.formatter import (
    full_package_markdown,
    kaikou_paste_markdown,
    package_markdown,
    topic_scores_markdown,
)
from engine.models import ContentPackage, RawSignal, TopicCandidate


def load_raw_signals(input_path: Path) -> list[RawSignal]:
    """Load raw signals from one JSON file or every JSON file in a folder."""

    paths = sorted(input_path.glob("*.json")) if input_path.is_dir() else [input_path]
    signals = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            signals.extend(RawSignal.from_dict(item) for item in data)
        else:
            signals.append(RawSignal.from_dict(data))
    return signals


def write_run_output(
    output_dir: Path,
    topics: list[TopicCandidate],
    packages: list[ContentPackage],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "00_topic_scores.md").write_text(topic_scores_markdown(topics), encoding="utf-8")
    for package in packages:
        (output_dir / f"{package.index:02d}_package.md").write_text(
            package_markdown(package),
            encoding="utf-8",
        )
    (output_dir / "full_package.md").write_text(full_package_markdown(packages), encoding="utf-8")
    (output_dir / "kaikou_paste.md").write_text(kaikou_paste_markdown(packages), encoding="utf-8")
    (output_dir / "run.json").write_text(
        json.dumps(
            {
                "topics": [asdict(topic) for topic in topics],
                "packages": [asdict(package) for package in packages],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
