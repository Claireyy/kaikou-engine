"""Normalize platform-specific signals into shared records."""

from __future__ import annotations

from engine.classifier import classify_signal
from engine.domain import classify_domain
from engine.models import RawSignal, TopicCandidate
from engine.scorer import score_signal, selection_status


def normalize_signals(signals: list[RawSignal]) -> list[TopicCandidate]:
    """Convert raw signals into scored topic candidates."""

    candidates = []
    for signal in signals:
        label, model = classify_signal(signal)
        domain = classify_domain(signal)
        scores = score_signal(signal)
        candidates.append(
            TopicCandidate(
                phenomenon=_phenomenon(signal),
                platform=signal.platform,
                source_title=signal.title,
                cognitive_label=label,
                model=model,
                scores=scores,
                selection_status=selection_status(scores["total"]),
                domain=domain,
                evidence=_evidence(signal),
            )
        )
    return candidates


def select_top_topics(candidates: list[TopicCandidate], limit: int = 4) -> list[TopicCandidate]:
    usable = [item for item in candidates if item.selection_status != "discard"]
    return sorted(usable, key=lambda item: item.total_score, reverse=True)[:limit]


def _phenomenon(signal: RawSignal) -> str:
    title = signal.title.strip()
    if title.endswith("。"):
        return title
    return f"{title}。"


def _evidence(signal: RawSignal) -> list[str]:
    evidence = []
    if signal.content_excerpt:
        evidence.append(signal.content_excerpt)
    evidence.extend(signal.comments[:3])
    return evidence
