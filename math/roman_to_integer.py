from typing import List
from colorama import Fore, Style


class Solution:

    def romanToInt(self, s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        subtractors = {
            'I': 'VX',
            'X': 'LC',
            'C': 'DM'
        }

        res = i = 0
        while i < len(s):
            if s[i] in subtractors and len(s) > i + 1 and s[i + 1] in subtractors[s[i]]:
                res += nums[s[i+1]] - nums[s[i]]
                i += 2
            else:
                res += nums[s[i]]
                i += 1

        return res


def test(vals):
    s = Solution()
    for v in vals:
        res = s.romanToInt(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ',
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("DCXXI", 621)
    ]

    test(vals)