"""Shared data models for the local pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


ScoreMap = dict[str, int]


@dataclass(frozen=True)
class RawSignal:
    platform: str
    title: str
    content_excerpt: str = ""
    source_url: str = ""
    captured_at: str = ""
    comments: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    collector: str = "manual"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "RawSignal":
        return cls(
            platform=str(data.get("platform", "unknown")),
            title=str(data.get("title", "")),
            content_excerpt=str(data.get("content_excerpt", "")),
            source_url=str(data.get("source_url", "")),
            captured_at=str(data.get("captured_at", "")),
            comments=[str(item) for item in data.get("comments", [])],
            metrics=dict(data.get("metrics", {})),
            collector=str(data.get("collector", "manual")),
        )


@dataclass(frozen=True)
class TopicCandidate:
    phenomenon: str
    platform: str
    source_title: str
    cognitive_label: str
    model: str
    scores: ScoreMap
    selection_status: str
    domain: str = "human_behavior"
    evidence: list[str] = field(default_factory=list)

    @property
    def total_score(self) -> int:
        return self.scores["total"]


@dataclass(frozen=True)
class ContentPackage:
    index: int
    topic: TopicCandidate
    script: str
    editing_script: list[dict[str, str]]
    subtitle_lines: list[str]
    publishing: dict[str, Any]
