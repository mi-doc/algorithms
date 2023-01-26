import unittest
from ..unique_paths import Solution


class UniquePathsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().uniquePaths
        return super().setUp()

    def test1(self):
        args = {
            'm': 3,
            'n': 7
        }
        expected_answer = 28

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'm': 3,
            'n': 2
        }
        expected_answer = 3

        res = self.sol(**args)
        assert res == expected_answer