"""Domain classification for Kaikou v6.1."""

from __future__ import annotations

from engine.models import RawSignal


DOMAIN_DISPLAY = {
    "human_behavior": "人类行为系统",
    "social_structure": "社会结构系统",
    "technology": "技术系统",
    "information": "信息系统",
    "time": "时间系统",
    "reality": "现实系统",
}


def classify_domain(signal: RawSignal) -> str:
    text = " ".join([signal.title, signal.content_excerpt, *signal.comments])

    if _contains_any(text, ("AI", "人工智能", "算法工具", "工具", "自动化", "模型", "替代", "门槛")):
        return "technology"
    if _contains_any(text, ("信息", "算法", "推荐", "流量", "内容", "同质化", "茧房", "注意力")):
        return "information"
    if _contains_any(text, ("长期", "周期", "复利", "延迟", "反馈", "即时", "时间", "看不到效果")):
        return "time"
    if _contains_any(text, ("规则", "环境", "失效", "不确定", "风险", "过去", "现在", "变化")):
        return "reality"
    if _contains_any(text, ("收入", "阶层", "城市", "成本", "教育", "学历", "房价", "工作形态", "回报")):
        return "social_structure"
    return "human_behavior"


def domain_display(domain: str) -> str:
    return DOMAIN_DISPLAY.get(domain, domain)


def _contains_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)
