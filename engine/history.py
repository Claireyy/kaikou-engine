"""Local history recording for generated runs."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from engine.models import ContentPackage


def append_history(history_path: Path, packages: list[ContentPackage], output_dir: Path) -> None:
    """Append selected topics and generated package metadata to a JSONL history file."""

    history_path.parent.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now().astimezone().isoformat(timespec="seconds")
    with history_path.open("a", encoding="utf-8") as file:
        for package in packages:
            record = {
                "run_at": run_at,
                "output_dir": str(output_dir),
                "package_index": package.index,
                "topic": asdict(package.topic),
                "titles": package.publishing.get("titles", []),
            }
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
