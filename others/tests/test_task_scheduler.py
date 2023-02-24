import unittest
from ..task_scheduler import Solution


class TaskSchedulerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().leastInterval
        return super().setUp()

    def test1(self):
        output = self.sol(
          tasks = ["A","A","A","B","B","B"], n = 2 
        )
        assert output == 8

    def test2(self):
        output = self.sol(
           tasks = ["A","A","A","B","B","B"], n = 0
        )
        assert output == 6

    def test3(self):
        output = self.sol(
           tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        )
        assert output == 16
