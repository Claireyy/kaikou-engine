"""Input validation for raw platform signals."""

from __future__ import annotations

from engine.models import RawSignal


REQUIRED_PLATFORMS = {"douyin", "xiaohongshu", "bilibili", "zhihu", "video_accounts"}


class ValidationError(ValueError):
    """Raised when a signal file cannot safely run through the pipeline."""


def validate_signals(signals: list[RawSignal]) -> None:
    errors = collect_validation_errors(signals)
    if errors:
        formatted = "\n".join(f"- {error}" for error in errors)
        raise ValidationError(f"Input validation failed:\n{formatted}")


def collect_validation_errors(signals: list[RawSignal]) -> list[str]:
    errors = []
    if not signals:
        errors.append("At least one signal is required.")
        return errors

    for index, signal in enumerate(signals, start=1):
        prefix = f"Signal {index}"
        if signal.platform not in REQUIRED_PLATFORMS:
            errors.append(
                f"{prefix}: platform must be one of {sorted(REQUIRED_PLATFORMS)}, got {signal.platform!r}."
            )
        if not signal.title.strip():
            errors.append(f"{prefix}: title is required.")
        if len(signal.title.strip()) > 80:
            errors.append(f"{prefix}: title should be 80 characters or fewer.")
        if not signal.content_excerpt.strip() and not any(comment.strip() for comment in signal.comments):
            errors.append(f"{prefix}: content_excerpt or at least one comment is required.")
        if len([comment for comment in signal.comments if comment.strip()]) < 2:
            errors.append(f"{prefix}: at least two non-empty comments are recommended.")
        if not signal.collector.strip():
            errors.append(f"{prefix}: collector is required.")
    return errors
