import unittest
from ..majority_element import Solution


class MajorityElementTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().majorityElement
        return super().setUp()

    def test1(self):
        output = self.sol(
          nums = [3,2,3]
        )
        assert output == 3

    def test2(self):
        output = self.sol(
          nums = [2,2,1,1,1,2,2]
        )
        assert output == 2

