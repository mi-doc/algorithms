import unittest
from ..top_k_frequent_elements import Solution


class TopKFrequentElementsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().topKFrequent4
        return super().setUp()

    def test1(self):
        args = {
            'nums': [1,1,1,2,2,3],
            'k': 2
        }
        expected_answer = [1,2]

        res = self.sol(**args)
        assert set(res) == set(expected_answer)


    def test2(self):
        args = {
            'nums': [3,0,1,0],
            'k': 1
        }
        expected_answer = [0]

        res = self.sol(**args)
        assert set(res) == set(expected_answer)

    def test3(self):
        args = {
            'nums': [1],
            'k': 1
        }
        expected_answer = [1]

        res = self.sol(**args)
        assert set(res) == set(expected_answer)