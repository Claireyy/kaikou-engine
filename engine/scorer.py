"""Viral topic scoring logic."""

from __future__ import annotations

from engine.models import RawSignal


SCORE_KEYS = (
    "real_world_frequency",
    "emotional_resonance",
    "cognitive_contradiction_strength",
    "comment_debate_potential",
    "speech_simplicity",
    "system_change_strength",
)


def score_signal(signal: RawSignal) -> dict[str, int]:
    """Score a signal on the v6.1 six-dimension viral rubric."""

    comments = signal.comments
    metrics = signal.metrics
    text = " ".join([signal.title, signal.content_excerpt, *comments])

    scores = {
        "real_world_frequency": _score_frequency(text, metrics),
        "emotional_resonance": _score_resonance(text, comments),
        "cognitive_contradiction_strength": _score_contradiction(text),
        "comment_debate_potential": _score_debate(comments, metrics),
        "speech_simplicity": _score_simplicity(signal.title),
        "system_change_strength": _score_system_change(text),
    }
    _apply_kaikou_fit(scores, text)
    scores["total"] = sum(scores[key] for key in SCORE_KEYS)
    return scores


def selection_status(total_score: int) -> str:
    if total_score >= 48:
        return "priority"
    if total_score >= 36:
        return "usable"
    return "discard"


def _score_frequency(text: str, metrics: dict[str, object]) -> int:
    score = 5
    if any(
        word in text
        for word in (
            "每天",
            "经常",
            "很多人",
            "上班",
            "亲密关系",
            "职场",
            "消费",
            "选择",
            "城市",
            "地域",
            "身份",
            "比较",
            "收入",
            "成本",
            "规则",
            "环境",
            "AI",
            "算法",
            "信息",
            "长期",
            "反馈",
        )
    ):
        score += 3
    if _metric(metrics, "likes") >= 10000 or _metric(metrics, "saves") >= 3000:
        score += 2
    return min(score, 10)


def _score_resonance(text: str, comments: list[str]) -> int:
    score = 4
    if any(
        word in text
        for word in (
            "焦虑",
            "委屈",
            "后悔",
            "不甘心",
            "累",
            "崩溃",
            "看不起",
            "优越感",
            "被定义",
            "不配",
            "证明自己",
        )
    ):
        score += 3
    if len(comments) >= 3:
        score += 2
    return min(score, 10)


def _score_contradiction(text: str) -> int:
    score = 4
    if any(word in text for word in ("明明", "但是", "越", "反而", "为什么", "却")):
        score += 4
    if any(word in text for word in ("以为", "结果", "不是", "真正", "一边", "一面", "表面")):
        score += 2
    if any(word in text for word in ("身份", "地域", "城市", "阶层", "专业", "学历", "消费观", "价值观")):
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


def _score_system_change(text: str) -> int:
    score = 2
    if any(
        word in text
        for word in (
            "结构",
            "变化",
            "规则",
            "环境",
            "失效",
            "替代",
            "门槛",
            "成本",
            "回报",
            "收入",
            "阶层",
            "城市",
            "教育",
            "工作形态",
            "AI",
            "算法",
            "信息过载",
            "长期",
            "周期",
            "不确定",
            "风险",
        )
    ):
        score += 5
    if any(word in text for word in ("过去", "现在", "越来越", "不再", "开始", "新环境", "旧经验")):
        score += 3
    return min(score, 10)


def _metric(metrics: dict[str, object], key: str) -> int:
    value = metrics.get(key)
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def _apply_kaikou_fit(scores: dict[str, int], text: str) -> None:
    """Favor cognition plus structural-change signals and cap generic hot topics."""

    if _has_kaikou_fit(text):
        return

    if _looks_like_generic_hot_topic(text):
        for key in SCORE_KEYS:
            scores[key] = min(scores[key], 5)


def _has_kaikou_fit(text: str) -> bool:
    fit_keywords = (
        "观念",
        "认知",
        "判断",
        "选择",
        "行为",
        "习惯",
        "身份",
        "地域",
        "城市",
        "阶层",
        "学历",
        "职场",
        "亲密关系",
        "消费",
        "自我",
        "比较",
        "优越感",
        "不配",
        "证明",
        "焦虑",
        "为什么",
        "明明",
        "反而",
        "越",
        "却",
        "结构",
        "规则",
        "环境",
        "失效",
        "成本",
        "回报",
        "AI",
        "算法",
        "信息",
        "长期",
        "系统",
    )
    return any(keyword in text for keyword in fit_keywords)


def _looks_like_generic_hot_topic(text: str) -> bool:
    generic_keywords = (
        "明星",
        "八卦",
        "比赛",
        "赛事",
        "开奖",
        "票房",
        "景区",
        "美食",
        "名菜",
        "菜品",
        "天气",
        "事故",
        "通报",
        "股价",
        "赌球",
    )
    return any(keyword in text for keyword in generic_keywords)
