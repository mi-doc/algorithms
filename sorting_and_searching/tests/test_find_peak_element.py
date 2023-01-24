import unittest
from ..find_peak_element import Solution


class FindPeakElementTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().findPeakElement2
        return super().setUp()

    def test1(self):
        args = {
            'nums': [1,2,3,1]
        }
        expected_answer = 2

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'nums': [1,2,1,3,5,6,4]
        }
        expected_answers = (1, 5)

        res = self.sol(**args)
        assert res in expected_answers 

    def test3(self):
        args = {
            'nums': [1]
        }
        expected_answer = 0

        res = self.sol(**args)
        assert res == expected_answer

    def test4(self):
        args = {
            'nums': [1, 2]
        }
        expected_answers = 1

        res = self.sol(**args)
        assert res == expected_answers 

    def test5(self):
        args = {
            'nums': [2, 1]
        }
        expected_answers = 0

        res = self.sol(**args)
        assert res == expected_answers 
    
    def test6(self):
        args = {
            'nums': [3,1,2]
        }
        expected_answers = (0,2)

        res = self.sol(**args)
        assert res in expected_answers 

    