import unittest
from ..kth_largest_element_in_an_array import Solution


class KthLargestElementInAnArrayTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().findKthLargest2
        return super().setUp()

    def test1(self):
        args = {
            'nums': [3,2,1,5,6,4],
            'k': 2
        }
        expected_answer = 5

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'nums': [3,2,3,1,2,4,5,5,6],
            'k': 4
        }
        expected_answer = 4

        res = self.sol(**args)
        assert res == expected_answer

    def test3(self):
        args = {
            'nums': [1,2,3],
            'k': 2
        }
        expected_answer = 2

        res = self.sol(**args)
        assert res == expected_answer