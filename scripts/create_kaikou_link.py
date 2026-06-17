"""Create a Kaikou task link from a generated run folder."""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_BASE_URL = "https://kaikou-e43.pages.dev/"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Kaikou task link from run.json.")
    parser.add_argument("run_dir", help="Run output folder containing run.json.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Kaikou base URL.")
    parser.add_argument("--copy", action="store_true", help="Copy the generated link to clipboard.")
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    payload = build_payload(run_dir)
    link, mode = create_link(args.base_url, payload)

    link_path = run_dir / "kaikou_link.txt"
    link_path.write_text(link + "\n", encoding="utf-8")

    print(f"{mode}: {link}")
    print(f"Saved to {link_path}")

    if args.copy:
        copy_to_clipboard(link)


def build_payload(run_dir: Path) -> dict[str, Any]:
    run_path = run_dir / "run.json"
    if not run_path.exists():
        raise SystemExit(f"Missing file: {run_path}")

    data = json.loads(run_path.read_text(encoding="utf-8"))
    packages = data.get("packages", [])
    if not packages:
        raise SystemExit(f"No packages found in {run_path}")

    tasks = []
    for package in packages:
        publishing = package.get("publishing", {})
        titles = publishing.get("titles") or []
        title = titles[2] if len(titles) >= 3 else package.get("topic", {}).get("phenomenon", "开口文案")
        tasks.append(
            {
                "title": str(title)[:80],
                "text": str(package.get("script", "")).strip(),
                "note": str(publishing.get("caption", "")).strip(),
            }
        )

    today = datetime.now().strftime("%Y-%m-%d")
    return {
        "title": f"开口 {today} 4 条",
        "text": tasks[0]["text"],
        "tasks": tasks,
        "font": 44,
        "speed": 34,
    }


def create_link(base_url: str, payload: dict[str, Any]) -> tuple[str, str]:
    base = base_url.rstrip("/") + "/"
    try:
        task_id = post_short_link(base, payload)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
        try:
            task_id = post_short_link_with_curl(base, payload)
        except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError):
            return make_hash_link(base, payload), "fallback-long-link"
    return urllib.parse.urljoin(base, f"?id={urllib.parse.quote(task_id)}"), "short-link"


def post_short_link(base_url: str, payload: dict[str, Any]) -> str:
    url = urllib.parse.urljoin(base_url, "/api/tasks")
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"content-type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))
    task_id = data.get("id")
    if not task_id:
        raise ValueError("Kaikou API did not return an id.")
    return str(task_id)


def post_short_link_with_curl(base_url: str, payload: dict[str, Any]) -> str:
    url = urllib.parse.urljoin(base_url, "/api/tasks")
    body = json.dumps(payload, ensure_ascii=False)
    result = subprocess.run(
        [
            "curl",
            "-sS",
            "-X",
            "POST",
            url,
            "-H",
            "content-type: application/json",
            "--data-binary",
            body,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(result.stdout)
    task_id = data.get("id")
    if not task_id:
        raise ValueError("Kaikou API did not return an id.")
    return str(task_id)


def make_hash_link(base_url: str, payload: dict[str, Any]) -> str:
    encoded = base64.urlsafe_b64encode(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).decode("ascii").rstrip("=")
    return f"{base_url.rstrip('/')}/#task={encoded}"


def copy_to_clipboard(text: str) -> None:
    try:
        subprocess.run(["pbcopy"], input=text, text=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        print("Could not copy link to clipboard. The link was still printed.", file=sys.stderr)


if __name__ == "__main__":
    main()
