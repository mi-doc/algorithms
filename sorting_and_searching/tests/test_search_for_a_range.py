import unittest
from ..search_for_a_range import Solution


class SearchForARangeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().searchRange2
        return super().setUp()

    def test1(self):
        args = {
            'nums':[5,7,7,8,8,10],
            'target': 8
        }
        expected_answer = [3,4]

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'nums':[5,7,7,8,8,10],
            'target': 6
        }
        expected_answer = [-1, -1]

        res = self.sol(**args)
        assert res == expected_answer

    def test3(self):
        args = {
            'nums': [],
            'target': 0
        }
        expected_answer = [-1, -1]

        res = self.sol(**args)
        assert res == expected_answer
    
    def test4(self):
        args = {
            'nums': [2,2],
            'target': 2
        }
        expected_answer = [0,1]

        res = self.sol(**args)
        assert res == expected_answer

    def test5(self):
        args = {
            'nums': [0,1,2,3,3,4,4,5,5,6,6,7,7,7,9,9,11,11,11,12,12,12,12],
            'target': 12
        }
        expected_answer = [19, 22]

        res = self.sol(**args)
        assert res == expected_answer
