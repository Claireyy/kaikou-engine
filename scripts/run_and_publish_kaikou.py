"""Run the daily pipeline and publish the result to Kaikou."""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from engine.pipeline import run_pipeline
from scripts.create_kaikou_link import DEFAULT_BASE_URL, create_link


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Kaikou Engine and publish a Kaikou short link.")
    parser.add_argument("--input", default="data/raw_signals/today.json", help="Raw signal input JSON.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Kaikou base URL.")
    parser.add_argument("--copy", action="store_true", help="Copy generated link to clipboard.")
    args = parser.parse_args()

    output_dir = Path("outputs") / "daily_runs" / datetime.now().strftime("%Y%m%d_%H%M%S")
    packages = run_pipeline(Path(args.input), output_dir)
    payload = _payload_from_packages(packages)
    link, mode = create_link(args.base_url, payload)

    link_path = output_dir / "kaikou_link.txt"
    link_path.write_text(link + "\n", encoding="utf-8")

    print(f"Generated {len(packages)} packages in {output_dir}")
    print(f"{mode}: {link}")
    print(f"Saved to {link_path}")

    if args.copy:
        _copy_to_clipboard(link)


def _payload_from_packages(packages) -> dict[str, object]:
    tasks = []
    for package in packages:
        titles = package.publishing.get("titles", [])
        title = titles[2] if len(titles) >= 3 else package.topic.phenomenon
        tasks.append(
            {
                "title": str(title)[:80],
                "text": package.script,
                "note": str(package.publishing.get("caption", "")),
            }
        )
    today = datetime.now().strftime("%Y-%m-%d")
    return {
        "title": f"开口 {today} 4 条",
        "text": tasks[0]["text"] if tasks else "",
        "tasks": tasks,
        "font": 44,
        "speed": 34,
    }


def _copy_to_clipboard(text: str) -> None:
    try:
        subprocess.run(["pbcopy"], input=text, text=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Could not copy link to clipboard. The link was still printed.", file=sys.stderr)


if __name__ == "__main__":
    main()
