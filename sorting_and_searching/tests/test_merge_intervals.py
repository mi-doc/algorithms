import unittest
from ..merge_intervals import Solution


class MergeIntervalsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().merge
        return super().setUp()

    def test1(self):
        args = {
            'intervals': [[1,3],[2,6],[8,10],[15,18]]
        }
        expected_answer = [[1,6],[8,10],[15,18]]

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'intervals': [[1,4],[4,5]]
        }
        expected_answer = [[1,5]]

        res = self.sol(**args)
        assert res == expected_answer
