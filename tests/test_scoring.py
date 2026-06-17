"""Tests for viral scoring behavior."""

import unittest

from engine.models import RawSignal
from engine.scorer import score_signal, selection_status


class ScoringTest(unittest.TestCase):
    def test_score_signal_returns_total(self):
        signal = RawSignal(
            platform="douyin",
            title="为什么很多人明明很累却停不下来",
            comments=["我也这样", "不一定", "每天都这样"],
            metrics={"likes": 20000, "comments": 1200},
        )

        scores = score_signal(signal)

        self.assertEqual(
            scores["total"],
            sum(
                scores[key]
                for key in (
                    "real_world_frequency",
                    "emotional_resonance",
                    "cognitive_contradiction_strength",
                    "comment_debate_potential",
                    "speech_simplicity",
                    "system_change_strength",
                )
            ),
        )

    def test_selection_status(self):
        self.assertEqual(selection_status(48), "priority")
        self.assertEqual(selection_status(36), "usable")
        self.assertEqual(selection_status(35), "discard")

    def test_system_change_strength_scores_structure(self):
        signal = RawSignal(
            platform="zhihu",
            title="为什么过去有效的方法现在开始失效",
            content_excerpt="规则变化让旧经验不再适用。",
            comments=["环境变了", "不只是个人问题"],
        )

        scores = score_signal(signal)

        self.assertGreaterEqual(scores["system_change_strength"], 8)


if __name__ == "__main__":
    unittest.main()
