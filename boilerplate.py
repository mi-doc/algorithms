from typing import List
from colorama import Fore, Style


class Solution:
    pass

def test(vals):
    s = Solution()
    for v in vals:
        res = 0
        # res = s.??
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ("input", "expected result"),
    ]

    test(vals)