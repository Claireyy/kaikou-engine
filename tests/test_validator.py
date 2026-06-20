"""Tests for input validation."""

import unittest

from engine.models import RawSignal
from engine.validator import collect_validation_errors


class ValidatorTest(unittest.TestCase):
    def test_valid_signal_has_no_errors(self):
        signal = RawSignal(
            platform="douyin",
            title="为什么越累越停不下来",
            content_excerpt="很多人下班后继续刷手机。",
            comments=["我也这样", "每天都这样"],
            collector="manual",
        )

        self.assertEqual(collect_validation_errors([signal]), [])

    def test_missing_title_is_error(self):
        signal = RawSignal(platform="douyin", title="", comments=["a", "b"])

        errors = collect_validation_errors([signal])

        self.assertTrue(any("title is required" in error for error in errors))

    def test_weibo_is_allowed_public_discussion_source(self):
        signal = RawSignal(
            platform="weibo",
            title="为什么旧经验在新环境开始失效",
            content_excerpt="评论区讨论规则变化。",
            comments=["环境变了", "不是个人问题"],
        )

        self.assertEqual(collect_validation_errors([signal]), [])


if __name__ == "__main__":
    unittest.main()
