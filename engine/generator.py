"""Content package generation logic."""

from __future__ import annotations

from engine.domain import domain_display
from engine.formatter import subtitle_lines
from engine.models import ContentPackage, TopicCandidate


MAX_SCRIPT_LINE_CHARS = 24

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
    script = _shorten_script(_script(topic))
    return ContentPackage(
        index=index,
        topic=topic,
        script=script,
        editing_script=_editing_script(topic),
        subtitle_lines=subtitle_lines(script),
        publishing=_publishing(topic),
    )


def _script(topic: TopicCandidate) -> str:
    if topic.domain != "human_behavior":
        return _system_script(topic)
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


def _system_script(topic: TopicCandidate) -> str:
    domain = domain_display(topic.domain)
    model = _model_display(topic)
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            f"这不是单纯的个人选择。",
            f"它更像是{domain}在变化。",
            *_system_scene_lines(topic),
            "过去有效的经验。",
            "放到现在未必还有效。",
            f"这里可以用{model}看。",
            "真正的问题不是人变差了。",
            "而是成本、回报和规则变了。",
            "人只是被新结构推着走。",
            "所以这件事的反常识点是。",
            "不要只问这个人怎么想。",
            "要问他所在的系统变成了什么。",
            "看懂结构。",
            "很多行为就没那么奇怪了。",
        ]
    )


def _default_script(topic: TopicCandidate) -> str:
    model = _model_display(topic)
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "表面上是在讨论一件事。",
            "其实是在暴露一种判断方式。",
            *_generic_scene_lines(),
            f"这里真正起作用的是{model}。",
            "人很多时候不是在表达观点。",
            "而是在用观点维持自己。",
            "所以争论的重点。",
            "往往不是谁对谁错。",
            "而是谁的自我解释被碰了一下。",
            "看懂这一层。",
            "评论区就不只是热闹。",
            "而是人在给自己找位置。",
        ]
    )


def _identity_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "这种话题最有意思的地方。",
            "不是事情本身有多大。",
            "而是它很容易叫出人的身份感。",
            *_identity_scene_lines(topic),
            "表面上大家在开玩笑。",
            "也在吐槽和站队。",
            "其实是在回答一个更隐蔽的问题。",
            "我属于哪里。",
            "我比谁更有资格。",
            "这就是身份滞后。",
            "一个人已经换了生活方式。",
            "但心里还需要旧标签撑场面。",
            "所以地域、学历、职业、品味。",
            "才会被讨论得特别激烈。",
            "因为大家争的不是事实。",
            "而是自己在事实里的位置。",
            "下次看到这种争论。",
            "可以先别急着判断谁玻璃心。",
            "先看哪一种身份被碰到了。",
        ]
    )


def _loss_aversion_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "很多看起来很理性的选择。",
            "背后其实不是在追求收益。",
            "而是在害怕失去。",
            *_loss_scene_lines(),
            "人一旦感觉自己正在变少。",
            "正在变亏。",
            "正在变不安全。",
            "就会特别想立刻做点什么。",
            "这就是损失厌恶。",
            "损失带来的刺痛。",
            "通常比收益带来的快乐更强。",
            "所以很多人行动。",
            "不是因为看懂了机会。",
            "而是受不了自己好像正在被落下。",
            "反直觉的是。",
            "越怕亏。",
            "越容易被新的风险牵着走。",
            "真正要看的不是该不该做。",
            "而是你是不是在用行动缓解不安。",
        ]
    )


def _attention_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "有些东西不是不存在。",
            "而是长期没有被看见。",
            *_attention_scene_lines(),
            "当一种人很少出现在作品里。",
            "一种生活很少被讲起。",
            "大家就会慢慢默认它不重要。",
            "这不是简单的偏见。",
            "而是注意力残留。",
            "我们会把经常看到的东西。",
            "当成更正常的东西。",
            "也当成更值得讲的东西。",
            "反过来。",
            "那些不常被看见的人。",
            "就会在公共想象里变得模糊。",
            "所以这个问题真正刺人的地方。",
            "不是有没有代表。",
            "而是谁一直被当成背景。",
        ]
    )


def _habit_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "很多人以为这是自控力问题。",
            "其实更像是场景触发。",
            *_habit_scene_lines(),
            "你不是每次都认真决定。",
            "我要这样做。",
            "而是到了那个时间。",
            "到了那个状态。",
            "身体就走进熟悉动作。",
            "这就是习惯回路。",
            "真正让人重复的。",
            "不是道理没听懂。",
            "而是提示、奖励和逃避感。",
            "已经连在一起。",
            "所以靠骂自己通常没用。",
            "你要改的不是人格。",
            "而是那个把你推回旧动作的场景。",
            "先看见触发点。",
            "才有可能换一个动作。",
        ]
    )


def _compounding_script(topic: TopicCandidate) -> str:
    return "\n".join(
        [
            f"你有没有发现，{_phenomenon_text(topic)}",
            "长期主义最折磨人的地方。",
            "不是要坚持。",
            "而是前面很长一段时间。",
            "都看不到反馈。",
            *_compounding_scene_lines(),
            "人会在没有反馈的时候怀疑自己。",
            "是不是我不行。",
            "是不是方向错了。",
            "是不是别人早就超过我了。",
            "这就是复利误读。",
            "我们总以为努力应该很快有回声。",
            "但很多变化的前期。",
            "就是沉默的。",
            "反直觉的是。",
            "真正让人放弃的常常不是失败。",
            "而是反馈太慢。",
            "所以你需要分清楚。",
            "自己是在修正方向。",
            "还是只是因为暂时看不到结果而慌了。",
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
            f"不是你变了，是系统变了",
            f"你以为是情绪，其实是{label}",
            f"{short}，背后是什么？",
        ],
        "caption": "\n".join(
            [
                f"很多人都经历过：{short}。",
                f"真正值得看的，是背后的{domain_display(topic.domain)}和{model}。",
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


def _phenomenon_text(topic: TopicCandidate) -> str:
    return topic.phenomenon.strip().rstrip("。！？!?")


def _generic_scene_lines() -> list[str]:
    return [
        "比如你看评论区。",
        "大家说的是观点。",
        "露出来的是判断习惯。",
    ]


def _identity_scene_lines(topic: TopicCandidate) -> list[str]:
    text = f"{topic.phenomenon} {' '.join(topic.evidence)}"
    if "城市" in text or "地域" in text or "上海" in text or "苏州" in text:
        return [
            "比如这件事里。",
            "大家表面上在争城市。",
            "其实是在争身份位置。",
        ]
    if "菜" in text or "美食" in text or "口味" in text:
        return [
            "比如这件事里。",
            "大家表面上在争口味。",
            "其实是在争品味身份。",
        ]
    return [
        "比如这件事里。",
        "大家表面上在争观点。",
        "其实是在争身份位置。",
    ]


def _loss_scene_lines() -> list[str]:
    return [
        "比如这件事里。",
        "钱可能还在账户里。",
        "但安全感先变少了。",
    ]


def _attention_scene_lines() -> list[str]:
    return [
        "比如这件事里。",
        "有些人不是没有生活。",
        "只是很少被作品看见。",
    ]


def _habit_scene_lines() -> list[str]:
    return [
        "比如这件事里。",
        "人不是突然失控。",
        "而是被熟悉场景推着走。",
    ]


def _compounding_scene_lines() -> list[str]:
    return [
        "比如这件事里。",
        "不是努力没有发生。",
        "而是反馈来得太慢。",
    ]


def _system_scene_lines(topic: TopicCandidate) -> list[str]:
    text = f"{topic.phenomenon} {' '.join(topic.evidence)}"
    if topic.domain == "technology":
        return [
            "比如 AI 让开始变容易。",
            "但也让真正变强更难。",
            "工具降低了门槛。",
            "也放大了判断差距。",
        ]
    if topic.domain == "information":
        return [
            "比如你以为自己在看世界。",
            "其实是在看被筛过的信息。",
            "信息越多。",
            "判断越容易被喂养。",
        ]
    if topic.domain == "time":
        return [
            "比如很多改变正在发生。",
            "但当下看不到效果。",
            "反馈太慢。",
            "人就容易误判。",
        ]
    if topic.domain == "social_structure":
        if "城市" in text:
            return [
                "比如同样努力的人。",
                "换一个城市。",
                "结果可能完全不同。",
                "不是努力消失了。",
            ]
        return [
            "比如收入、教育和工作。",
            "看起来是个人选择。",
            "其实背后有成本结构。",
            "也有回报结构。",
        ]
    if topic.domain == "reality":
        return [
            "比如很多旧方法。",
            "以前很有效。",
            "现在开始失效。",
            "不是人突然不行了。",
        ]
    return _generic_scene_lines()


def _shorten_script(script: str) -> str:
    lines = []
    for raw_line in script.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        lines.extend(_split_long_script_line(line))
    return "\n".join(lines)


def _split_long_script_line(line: str) -> list[str]:
    if len(line) <= MAX_SCRIPT_LINE_CHARS:
        return [line]

    pieces = []
    current = ""
    for char in line:
        current += char
        if char in "，,：:；;。！？!?" and len(current) >= 8:
            pieces.append(_trim_sentence_mark(current))
            current = ""
        elif len(current) >= MAX_SCRIPT_LINE_CHARS and _is_breakable(current):
            pieces.append(_trim_sentence_mark(current))
            current = ""
    if current:
        pieces.append(_trim_sentence_mark(current))
    return [piece for piece in pieces if piece]


def _trim_sentence_mark(value: str) -> str:
    return value.strip().strip("，,：:；;。！？!?")


def _is_breakable(value: str) -> bool:
    return value[-1] in "的了是在和与把被就也都不人事里上中下"
