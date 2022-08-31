from typing import List
from colorama import Fore, Style
from collections import deque, Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        max_sbstr = 0
        for c in s:
            while q and c in q:
                q.popleft()
            q.append(c)
            max_sbstr = max(len(q), max_sbstr)

        return max_sbstr

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        Better solution from leetcode
        """
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


def test(vals):
    s = Solution()
    for v in vals:
        res = s.lengthOfLongestSubstring2(v[0])
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("aab", 2),
        ("dvdf", 3)
    ]

    test(vals)