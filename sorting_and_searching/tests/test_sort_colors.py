import unittest
from ..sort_colors import Solution


class SortColorsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().sortColors
        return super().setUp()

    def test1(self):
        nums = [2,0,2,1,1,0]
        self.sol(nums)
        assert nums == [0,0,1,1,2,2]

    def test2(self):
        nums = [2,0,1]
        self.sol(nums)
        assert nums == [0,1,2]
