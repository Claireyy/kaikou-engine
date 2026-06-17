"""Topic and script deduplication helpers."""

from __future__ import annotations

import re

from engine.models import TopicCandidate


def deduplicate_topics(candidates: list[TopicCandidate]) -> list[TopicCandidate]:
    """Remove near-duplicate topics with a simple normalized text key."""

    seen = set()
    unique = []
    for candidate in candidates:
        key = _topic_key(candidate.phenomenon)
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate)
    return unique


def _topic_key(value: str) -> str:
    normalized = re.sub(r"\s+", "", value.lower())
    return normalized[:40]
