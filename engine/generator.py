"""Content package generation logic."""

from __future__ import annotations

from engine.formatter import subtitle_lines
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


def generate_packages(topics: list[TopicCandidate]) -> list[ContentPackage]:
    return [_generate_package(index, topic) for index, topic in enumerate(topics, start=1)]


def _generate_package(index: int, topic: TopicCandidate) -> ContentPackage:
    script = _script(topic)
    return ContentPackage(
        index=index,
        topic=topic,
        script=script,
        editing_script=_editing_script(topic),
        subtitle_lines=subtitle_lines(script),
        publishing=_publishing(topic),
    )


def _script(topic: TopicCandidate) -> str:
    model = _model_display(topic)
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "它看起来像是一个情绪问题，但更像是一个判断被环境带偏的瞬间。",
            f"比如你在生活里反复遇到类似场景：{_first_evidence(topic)}",
            f"这里真正起作用的不是大道理，而是{model}。",
            "人不是先想清楚再行动，很多时候是先被场景推着走，然后再给自己找解释。",
            "所以反直觉的地方在于：你越急着纠正自己，越容易忽略那个让你重复反应的环境。",
            "下次再遇到这种时刻，可以先别急着评价自己，先看看自己被什么东西带进去了。",
        ]
    )


def _editing_script(topic: TopicCandidate) -> list[dict[str, str]]:
    return [
        {
            "scene": "Scene 1",
            "time": "0-5s",
            "voice": f"开头现象：{topic.phenomenon}",
            "visual": "手机手持感，拍一个和选题有关的真实日常瞬间。",
        },
        {
            "scene": "Scene 2",
            "time": "5-20s",
            "voice": "具体生活场景。",
            "visual": "办公室、街头或家里，呈现这个行为发生的真实环境。",
        },
        {
            "scene": "Scene 3",
            "time": "20-40s",
            "voice": f"只用{_model_display(topic)}解释，不叠加其他模型。",
            "visual": "真实细节近景，不要抽象图形，不要 AI 视觉感。",
        },
        {
            "scene": "Scene 4",
            "time": "40-55s",
            "voice": "反直觉洞察。",
            "visual": "一个停顿、表情变化或很小的行为转向。",
        },
        {
            "scene": "Scene 5",
            "time": "55-60s",
            "voice": "柔和收尾，不讲道理。",
            "visual": "自然结束镜头，继续保持手持和真实感。",
        },
    ]


def _publishing(topic: TopicCandidate) -> dict[str, object]:
    short = topic.phenomenon.rstrip("。")
    label = LABEL_DISPLAY.get(topic.cognitive_label, topic.cognitive_label)
    model = _model_display(topic)
    return {
        "titles": [
            f"为什么你总会遇到这种事？",
            f"你以为是情绪，其实是{label}",
            f"{short}，背后是什么？",
        ],
        "caption": "\n".join(
            [
                f"很多人都经历过：{short}。",
                f"真正值得看的，是背后的{model}。",
                "你最近有没有类似的瞬间？",
            ]
        ),
        "hashtags": ["认知", "决策", "行为观察", "日常生活", "感知"],
    }


def _first_evidence(topic: TopicCandidate) -> str:
    if topic.evidence:
        return topic.evidence[0]
    return topic.source_title


def _model_display(topic: TopicCandidate) -> str:
    return MODEL_DISPLAY.get(topic.model, topic.model)
