from typing import List
from colorama import Fore, Style


class Solution:
    """
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    Given two integers x and y, return the Hamming distance between them.
    """
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = format(x, 'b'), format(y, 'b')
        max_len = max(len(x), len(y))
        res = 0
        for i in range(-1, -max_len - 1, -1):
            num1 = x[i] if len(x) >= abs(i) else '0'
            num2 = y[i] if len(y) >= abs(i) else '0'

            if num1 != num2:
                res += 1
        return res

    def hammingDistance2(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y


def test(vals):
    s = Solution()
    for v in vals:
        res = s.hammingDistance2(*v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ',
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([1,4], 2),
        ([3,1], 1),
        ([11,21], 4),
        ([0,0], 0),
        ([0,1], 1)
    ]

    test(vals)