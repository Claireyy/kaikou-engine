"""Validate a raw signal input file before running the pipeline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from engine.storage import load_raw_signals
from engine.validator import ValidationError, validate_signals


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Kaikou raw signal input.")
    parser.add_argument("input", help="JSON file or folder containing raw signals.")
    args = parser.parse_args()

    signals = load_raw_signals(Path(args.input))
    try:
        validate_signals(signals)
    except ValidationError as error:
        print(str(error))
        raise SystemExit(1) from error

    print(f"OK: {len(signals)} signals are valid.")


if __name__ == "__main__":
    main()
