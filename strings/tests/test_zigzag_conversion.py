import unittest
from ..zigzag_conversion import Solution


class ZigzagConversionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().convert
        return super().setUp()

    def test1(self):
        output = self.sol(
          s = "PAYPALISHIRING", numRows = 3 
        )
        assert output == "PAHNAPLSIIGYIR"

    def test2(self):
        output = self.sol(
          s = "PAYPALISHIRING", numRows = 4 
        )
        assert output == "PINALSIGYAHRPI"

