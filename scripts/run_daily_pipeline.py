"""Run the daily Kaikou Engine pipeline."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from engine.pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Kaikou Engine local pipeline.")
    parser.add_argument(
        "--input",
        default="data/samples/sample_signals.json",
        help="JSON file or folder containing raw signals.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output folder. Defaults to outputs/daily_runs/<timestamp>.",
    )
    parser.add_argument("--count", type=int, default=4, help="Number of packages to generate.")
    parser.add_argument(
        "--history",
        default="data/history/history.jsonl",
        help="History JSONL path. Use --history none to disable.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output) if args.output else _default_output_dir()
    history_path = None if args.history == "none" else Path(args.history)
    packages = run_pipeline(
        Path(args.input),
        output_dir,
        output_count=args.count,
        history_path=history_path,
    )
    print(f"Generated {len(packages)} packages in {output_dir}")


def _default_output_dir() -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path("outputs") / "daily_runs" / timestamp


if __name__ == "__main__":
    main()
