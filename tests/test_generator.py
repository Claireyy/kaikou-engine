"""Tests for generated script constraints."""

import unittest

from engine.generator import MAX_SCRIPT_LINE_CHARS, generate_packages
from engine.models import TopicCandidate


class GeneratorTest(unittest.TestCase):
    def test_generated_script_lines_are_short(self):
        topic = TopicCandidate(
            phenomenon="沪苏争霸：上海与苏州的地域竞争二创视频爆火。",
            platform="douyin",
            source_title="沪苏争霸",
            cognitive_label="Identity mismatch",
            model="Identity lag",
            scores={"total": 41},
            selection_status="priority",
            evidence=[
                "评论区演变为真实的地域自豪感对决，大家争的不是事实，而是自己在事实里的位置。"
            ],
        )

        package = generate_packages([topic])[0]

        self.assertTrue(all(len(line) <= MAX_SCRIPT_LINE_CHARS for line in package.script.splitlines()))


if __name__ == "__main__":
    unittest.main()
