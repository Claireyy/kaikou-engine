"""Cognitive classification logic."""

from __future__ import annotations

from engine.models import RawSignal


LABELS = (
    "Judgment error",
    "Action distortion",
    "Identity mismatch",
    "Feedback delay",
    "Perception bias",
)

MODELS = (
    "Specific Knowledge",
    "Judgment",
    "Identity lag",
    "Compounding error",
    "Cognitive dissonance",
    "Attention residue",
    "Habit loop",
    "Framing effect",
    "Loss aversion",
    "Anchoring bias",
    "Framing bias",
)


def classify_signal(signal: RawSignal) -> tuple[str, str]:
    """Return one cognitive label and one model for a signal."""

    text = _combined_text(signal)

    if _contains_any(text, ("身份", "人设", "标签", "不配", "像不像", "自我")):
        return "Identity mismatch", "Identity lag"
    if _contains_any(text, ("回报", "长期", "复利", "反馈", "看不到", "等待")):
        return "Feedback delay", "Compounding error"
    if _contains_any(text, ("拖延", "明天", "坚持", "习惯", "控制不住", "刷")):
        return "Action distortion", "Habit loop"
    if _contains_any(text, ("亏", "后悔", "舍不得", "损失", "沉没", "白花")):
        return "Judgment error", "Loss aversion"
    if _contains_any(text, ("注意力", "分心", "焦虑", "信息", "比较", "看到")):
        return "Perception bias", "Attention residue"

    return "Judgment error", "Judgment"


def _combined_text(signal: RawSignal) -> str:
    return " ".join([signal.title, signal.content_excerpt, *signal.comments])


def _contains_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)
