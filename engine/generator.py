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
    if topic.model == "Identity lag":
        return _identity_script(topic)
    if topic.model == "Loss aversion":
        return _loss_aversion_script(topic)
    if topic.model == "Attention residue":
        return _attention_script(topic)
    if topic.model == "Habit loop":
        return _habit_script(topic)
    if topic.model == "Compounding error":
        return _compounding_script(topic)
    return _default_script(topic)


def _default_script(topic: TopicCandidate) -> str:
    model = _model_display(topic)
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "表面上大家在讨论一件事，其实是在暴露一种稳定的判断方式。",
            f"比如你在生活里反复遇到类似场景：{_first_evidence(topic)}",
            f"这里真正起作用的是{model}。",
            "人很多时候不是在表达观点，而是在用观点维持一个自洽的自己。",
            "所以反直觉的是，争论的重点往往不是谁对谁错，而是谁的自我解释被碰了一下。",
            "看懂这一层，很多评论区就不只是热闹，而是人在给自己找位置。",
        ]
    )


def _identity_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "这种话题最有意思的地方，不是事情本身有多大，而是它很容易把人的身份感叫出来。",
            f"比如这件事里：{_first_evidence(topic)}",
            "表面上大家在开玩笑、吐槽、站队，其实是在回答一个更隐蔽的问题：我属于哪里，我比谁更有资格。",
            "这就是身份滞后。",
            "一个人已经换了生活方式，但心里还需要旧标签给自己撑场面。",
            "所以地域、学历、职业、品味这些东西，才会被讨论得特别激烈。",
            "因为大家争的不是事实，而是自己在那个事实里的位置。",
            "下次看到这种争论，可以先别急着判断谁玻璃心，先看哪一种身份被碰到了。",
        ]
    )


def _loss_aversion_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "很多看起来很理性的选择，背后其实不是在追求收益，而是在害怕失去。",
            f"比如这件事里：{_first_evidence(topic)}",
            "人一旦感觉自己正在变少、变亏、变不安全，就会特别想立刻做点什么。",
            "这就是损失厌恶。",
            "损失带来的刺痛，通常比同等收益带来的快乐更强。",
            "所以很多人不是因为看懂了机会才行动，而是因为受不了自己好像正在被落下。",
            "反直觉的是，越怕亏，越容易被一个新的风险牵着走。",
            "真正要看的不是这件事该不该做，而是你是不是在用行动缓解不安。",
        ]
    )


def _attention_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "有些东西不是不存在，而是长期没有被镜头、叙事和讨论看见。",
            f"比如这件事里：{_first_evidence(topic)}",
            "当一种人、一种生活、一种路径很少出现在作品里，大家就会慢慢默认它不重要。",
            "这不是简单的偏见，而是注意力残留。",
            "我们会把经常看到的东西，当成更正常、更高级、更值得讲的东西。",
            "反过来，那些不常被看见的人，就会在公共想象里变得模糊。",
            "所以这个问题真正刺人的地方，不是有没有代表，而是谁一直被当成背景。",
            "当一个群体开始问为什么没有我，其实是在要回被看见的位置。",
        ]
    )


def _habit_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "很多人以为这是自控力问题，其实更像是一个场景自动触发的反应。",
            f"比如这件事里：{_first_evidence(topic)}",
            "你不是每次都认真决定要这样做，而是到了那个时间、那个状态，身体就自动走进熟悉动作。",
            "这就是习惯回路。",
            "真正让人重复的，不是道理没听懂，而是提示、奖励和逃避感已经连在一起。",
            "所以反直觉的是，靠骂自己通常没用。",
            "你要改的不是人格，而是那个一出现就把你推回旧动作的场景。",
            "先看见触发点，才有可能真的换一个动作。",
        ]
    )


def _compounding_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{topic.phenomenon}",
            "长期主义最折磨人的地方，不是要坚持，而是前面很长一段时间都看不到反馈。",
            f"比如这件事里：{_first_evidence(topic)}",
            "人会在没有反馈的时候开始怀疑自己：是不是我不行，是不是方向错了，是不是别人早就超过我了。",
            "这就是复利误读。",
            "我们总以为努力应该很快给一个回声，但很多变化前期就是沉默的。",
            "反直觉的是，真正让人放弃的常常不是失败，而是反馈太慢。",
            "所以你需要分清楚，自己是在修正方向，还是只是因为暂时看不到结果而慌了。",
            "有些东西不是没有发生，只是还没到能被你看见的时候。",
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
