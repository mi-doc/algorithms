from typing import List
from colorama import Fore, Style


class Solution:
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    '''
    def isValid(self, s: str) -> bool:
        pars = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        for p in s:
            if p in pars:
                stack.append(p)
            elif not stack or pars[stack.pop()] != p:
                return False

        return not stack


def test(vals):
    s = Solution()
    for v in vals:
        res = s.isValid(v[0])
        print(
            v,
            ' -> ',
            Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ("()", True),
        ("(){}[]", True),
        ("([]{})", True),
        ("([]{])", False),
        ("([])[{}]", True),
        ("([}){()}", False),
        ("[)", False),
        ("[(){}({})]", True),
        ("[(){}([})]", False),
        ["[", False],
        ["]", False]
    ]

    test(vals)


