"""Copy a run's Kaikou paste package to the macOS clipboard."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy kaikou_paste.md from a run folder.")
    parser.add_argument("run_dir", help="Run output folder containing kaikou_paste.md.")
    args = parser.parse_args()

    paste_path = Path(args.run_dir) / "kaikou_paste.md"
    if not paste_path.exists():
        raise SystemExit(f"Missing file: {paste_path}")

    content = paste_path.read_text(encoding="utf-8")
    try:
        subprocess.run(["pbcopy"], input=content, text=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise SystemExit(
            f"Could not copy to clipboard. Open and copy manually: {paste_path}"
        ) from error
    print(f"Copied {paste_path} to clipboard.")


if __name__ == "__main__":
    main()
