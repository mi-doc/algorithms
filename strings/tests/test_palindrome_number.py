import unittest
from ..palindrome_number import Solution


class PalindromeNumberTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().isPalindrome
        return super().setUp()

    def test1(self):
        output = self.sol(
          x = 121 
        )
        assert output == True

    def test2(self):
        output = self.sol(
           x = -121
        )
        assert output == False

    def test3(self):
        output = self.sol(
           x = 10
        )
        assert output == False

    def test4(self):
        output = self.sol(
          x = 12321 
        )
        assert output == True