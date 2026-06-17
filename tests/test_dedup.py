"""Tests for topic and script deduplication."""

import unittest

from engine.dedup import deduplicate_topics
from engine.models import TopicCandidate


class DedupTest(unittest.TestCase):
    def test_deduplicate_topics_removes_same_phenomenon(self):
        topic = TopicCandidate(
            phenomenon="很多人明明很累却停不下来。",
            platform="douyin",
            source_title="很多人明明很累却停不下来",
            cognitive_label="Action distortion",
            model="Habit loop",
            scores={"total": 40},
            selection_status="priority",
        )

        self.assertEqual(deduplicate_topics([topic, topic]), [topic])


if __name__ == "__main__":
    unittest.main()
