"""Viral topic scoring logic."""

from __future__ import annotations

from engine.models import RawSignal


SCORE_KEYS = (
    "real_world_frequency",
    "emotional_resonance",
    "cognitive_contradiction_strength",
    "comment_debate_potential",
    "speech_simplicity",
)


def score_signal(signal: RawSignal) -> dict[str, int]:
    """Score a signal on the v6.0 five-dimension viral rubric."""

    comments = signal.comments
    metrics = signal.metrics
    text = " ".join([signal.title, signal.content_excerpt, *comments])

    scores = {
        "real_world_frequency": _score_frequency(text, metrics),
        "emotional_resonance": _score_resonance(text, comments),
        "cognitive_contradiction_strength": _score_contradiction(text),
        "comment_debate_potential": _score_debate(comments, metrics),
        "speech_simplicity": _score_simplicity(signal.title),
    }
    scores["total"] = sum(scores[key] for key in SCORE_KEYS)
    return scores


def selection_status(total_score: int) -> str:
    if total_score >= 40:
        return "priority"
    if total_score >= 30:
        return "usable"
    return "discard"


def _score_frequency(text: str, metrics: dict[str, object]) -> int:
    score = 5
    if any(word in text for word in ("每天", "经常", "很多人", "上班", "亲密关系", "职场")):
        score += 3
    if _metric(metrics, "likes") >= 10000 or _metric(metrics, "saves") >= 3000:
        score += 2
    return min(score, 10)


def _score_resonance(text: str, comments: list[str]) -> int:
    score = 4
    if any(word in text for word in ("焦虑", "委屈", "后悔", "不甘心", "累", "崩溃")):
        score += 3
    if len(comments) >= 3:
        score += 2
    return min(score, 10)


def _score_contradiction(text: str) -> int:
    score = 4
    if any(word in text for word in ("明明", "但是", "越", "反而", "为什么", "却")):
        score += 4
    if any(word in text for word in ("以为", "结果", "不是", "真正")):
        score += 2
    return min(score, 10)


def _score_debate(comments: list[str], metrics: dict[str, object]) -> int:
    score = 4
    joined = " ".join(comments)
    if any(word in joined for word in ("不一定", "我不同意", "看情况", "可是", "凭什么")):
        score += 3
    if len(comments) >= 5 or _metric(metrics, "comments") >= 1000:
        score += 3
    return min(score, 10)


def _score_simplicity(title: str) -> int:
    length = len(title.strip())
    if length <= 22:
        return 10
    if length <= 36:
        return 8
    if length <= 50:
        return 6
    return 4


def _metric(metrics: dict[str, object], key: str) -> int:
    value = metrics.get(key)
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0
