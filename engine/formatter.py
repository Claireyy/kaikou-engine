"""Output formatting helpers."""

from __future__ import annotations

import re

from engine.models import ContentPackage, TopicCandidate


def subtitle_lines(script: str, max_chars: int = 15) -> list[str]:
    """Split script into short subtitle-ready lines."""

    lines = []
    for paragraph in script.splitlines():
        for sentence in _split_sentences(paragraph):
            lines.extend(_split_sentence(sentence, max_chars=max_chars))
    return lines


def topic_scores_markdown(topics: list[TopicCandidate]) -> str:
    rows = [
        "# Topic Scores",
        "",
        "| Rank | Phenomenon | Label | Model | Total | Status |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for rank, topic in enumerate(topics, start=1):
        rows.append(
            f"| {rank} | {topic.phenomenon} | {topic.cognitive_label} | "
            f"{topic.model} | {topic.total_score} | {topic.selection_status} |"
        )
    rows.append("")
    return "\n".join(rows)


def package_markdown(package: ContentPackage) -> str:
    topic = package.topic
    sections = [
        f"# Package {package.index}: {topic.phenomenon}",
        "",
        "## Topic",
        "",
        f"- Platform: {topic.platform}",
        f"- Cognitive label: {topic.cognitive_label}",
        f"- Model: {topic.model}",
        f"- Score: {topic.total_score}/50",
        "",
        "## Script",
        "",
        package.script,
        "",
        "## Editing Script",
        "",
    ]
    for scene in package.editing_script:
        sections.extend(
            [
                f"### {scene['scene']} ({scene['time']})",
                "",
                f"- Voice: {scene['voice']}",
                f"- Visual: {scene['visual']}",
                "",
            ]
        )
    sections.extend(
        [
            "## Subtitles",
            "",
            "\n".join(package.subtitle_lines),
            "",
            "## Publishing",
            "",
            "### Titles",
            "",
        ]
    )
    for title in package.publishing["titles"]:
        sections.append(f"- {title}")
    sections.extend(
        [
            "",
            "### Caption",
            "",
            str(package.publishing["caption"]),
            "",
            "### Hashtags",
            "",
            " ".join(f"#{tag}" for tag in package.publishing["hashtags"]),
            "",
        ]
    )
    return "\n".join(sections)


def full_package_markdown(packages: list[ContentPackage]) -> str:
    parts = ["# Kaikou Daily Package", ""]
    for package in packages:
        parts.append(package_markdown(package))
        parts.append("")
        parts.append("---")
        parts.append("")
    return "\n".join(parts)


def _split_sentences(text: str) -> list[str]:
    cleaned = text.strip()
    if not cleaned:
        return []
    parts = re.split(r"[。！？!?；;]", cleaned)
    return [part.strip(" ，,：:") for part in parts if part.strip(" ，,：:")]


def _split_sentence(sentence: str, max_chars: int) -> list[str]:
    if len(sentence) <= max_chars:
        return [sentence]

    chunks = []
    current = ""
    for part in re.split(r"([，,：:、])", sentence):
        if part in ("，", ",", "：", ":", "、"):
            continue
        piece = part.strip()
        if not piece:
            continue
        if len(current) + len(piece) <= max_chars:
            current += piece
            continue
        if current:
            chunks.append(current)
            current = ""
        while len(piece) > max_chars:
            chunks.append(piece[:max_chars])
            piece = piece[max_chars:]
        current = piece
    if current:
        chunks.append(current)
    return chunks
