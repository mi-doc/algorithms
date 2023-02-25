import unittest
from ..count_and_say import Solution


class CountAndSayTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().countAndSay
        return super().setUp()

    def test1(self):
        output = self.sol(
           n = 1
        )
        assert output == '1'

    def test2(self):
        output = self.sol(
           n = 4
        )
        assert output == "1211"

