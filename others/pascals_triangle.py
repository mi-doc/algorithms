from typing import List
from colorama import Fore, Style


class Solution:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return [[]]

        triangle = [[1]]
        for _ in range(numRows - 1):
            prev = triangle[-1]
            row = [1]
            for i in range(1, len(prev)):
                row.append(prev[i-1] + prev[i])
            row.append(1)
            triangle.append(row)

        return triangle


def test(vals):
    s = Solution()
    for v in vals:
        res = s.generate(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ',
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
        (1, [[1]]),
        (0, [[]])
    ]

    test(vals)

