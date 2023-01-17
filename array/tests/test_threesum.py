import unittest
from ..threesum import Solution


class ThreeSumTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.nums = [
           ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
           ([0,0,0], [[0,0,0]]),
           ([1,2,5], []),
           ([1,1,1], []),
           ([1,2,-2,-1], []),
           ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]])

        ]
        self.sol = Solution()
        return super().setUp()

    def test(self):
        for num in self.nums:
            res = self.sol.threeSum(num[0])
            assert res == set(tuple(x) for x in num[1])
    