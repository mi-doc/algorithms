import unittest
from ..jump_game import Solution


class JumpGameTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().canJump2
        return super().setUp()

    def test1(self):
        args = {
            'nums': [2,3,1,1,4]
        }
        expected_answer = True

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'nums': [3,2,1,0,4]
        }
        expected_answer = False

        res = self.sol(**args)
        assert res == expected_answer

