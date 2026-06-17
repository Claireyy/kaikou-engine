"""Copy Kaikou editor-ready text to the macOS clipboard."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy kaikou_editor_text.txt from a run folder.")
    parser.add_argument("run_dir", help="Run output folder containing kaikou_editor_text.txt.")
    args = parser.parse_args()

    text_path = Path(args.run_dir) / "kaikou_editor_text.txt"
    if not text_path.exists():
        raise SystemExit(f"Missing file: {text_path}")

    content = text_path.read_text(encoding="utf-8")
    try:
        subprocess.run(["pbcopy"], input=content, text=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Could not copy to clipboard. Open and copy manually: {text_path}") from error
    print(f"Copied {text_path} to clipboard.")


if __name__ == "__main__":
    main()
