import unittest
from ..longest_inc_subsequence import Solution


class LongestIncSubsequenceTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().lengthOfLIS
        return super().setUp()

    def test1(self):
        args = {
            'nums': [10,9,2,5,3,7,101,18]
        }
        expected_answer = 4

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'nums': [0,1,0,3,2,3]
        }
        expected_answer = 4

        res = self.sol(**args)
        assert res == expected_answer

    def test3(self):
        args = {
           'nums': [7,7,7,7,7,7,7]
        }
        expected_answer = 1

        res = self.sol(**args)
        assert res == expected_answer