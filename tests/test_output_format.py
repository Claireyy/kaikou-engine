"""Tests for generated output structure."""

import unittest

from engine.formatter import subtitle_lines


class OutputFormatTest(unittest.TestCase):
    def test_subtitle_lines_respects_limit(self):
        lines = subtitle_lines("这是一句适合短视频口播的测试文案", max_chars=6)

        self.assertTrue(all(len(line) <= 6 for line in lines))


if __name__ == "__main__":
    unittest.main()
