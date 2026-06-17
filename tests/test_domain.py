"""Tests for v6.1 domain classification."""

import unittest

from engine.domain import classify_domain
from engine.models import RawSignal


class DomainTest(unittest.TestCase):
    def test_classifies_technology_domain(self):
        signal = RawSignal(platform="bilibili", title="为什么AI让人更容易开始但更难变强")

        self.assertEqual(classify_domain(signal), "technology")

    def test_classifies_social_structure_domain(self):
        signal = RawSignal(platform="zhihu", title="为什么同样努力的人城市不同结果完全不同")

        self.assertEqual(classify_domain(signal), "social_structure")


if __name__ == "__main__":
    unittest.main()
