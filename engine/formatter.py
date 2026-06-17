"""Output formatting helpers."""

from __future__ import annotations

import re

from engine.models import ContentPackage, TopicCandidate


LABEL_DISPLAY = {
    "Judgment error": "判断误差",
    "Action distortion": "行动变形",
    "Identity mismatch": "身份错位",
    "Feedback delay": "反馈延迟",
    "Perception bias": "感知偏差",
}

MODEL_DISPLAY = {
    "Specific Knowledge": "特定知识",
    "Judgment": "判断力",
    "Identity lag": "身份滞后",
    "Compounding error": "复利误读",
    "Cognitive dissonance": "认知失调",
    "Attention residue": "注意力残留",
    "Habit loop": "习惯回路",
    "Framing effect": "框架效应",
    "Loss aversion": "损失厌恶",
    "Anchoring bias": "锚定偏差",
    "Framing bias": "框架偏差",
}


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


def kaikou_paste_markdown(packages: list[ContentPackage]) -> str:
    """Compact paste-ready format for the Kaikou site/editor."""

    parts = [
        "# Kaikou Paste Package",
        "",
        "复制下面内容到 Kaikou。每条是一个完整短视频文案包。",
        "",
    ]
    for package in packages:
        topic = package.topic
        titles = package.publishing["titles"]
        parts.extend(
            [
                f"## {package.index}. {topic.phenomenon}",
                "",
                f"认知标签：{_label_display(topic)}",
                f"认知模型：{_model_display(topic)}",
                f"评分：{topic.total_score}/50",
                "",
                "标题：",
                f"1. {titles[0]}",
                f"2. {titles[1]}",
                f"3. {titles[2]}",
                "",
                "口播文案：",
                package.script,
                "",
                "字幕：",
                "\n".join(package.subtitle_lines),
                "",
                "发布文案：",
                str(package.publishing["caption"]),
                "",
                "标签：",
                " ".join(f"#{tag}" for tag in package.publishing["hashtags"]),
                "",
                "---",
                "",
            ]
        )
    return "\n".join(parts)


def _label_display(topic: TopicCandidate) -> str:
    return LABEL_DISPLAY.get(topic.cognitive_label, topic.cognitive_label)


def _model_display(topic: TopicCandidate) -> str:
    return MODEL_DISPLAY.get(topic.model, topic.model)


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
