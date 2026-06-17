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
                )
            ),
        )

    def test_selection_status(self):
        self.assertEqual(selection_status(41), "priority")
        self.assertEqual(selection_status(30), "usable")
        self.assertEqual(selection_status(29), "discard")


if __name__ == "__main__":
    unittest.main()
