from typing import List
from colorama import Fore, Style
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        
        return list(anagrams.values())

    def groupAnagrams2(self, strs):
        """
        Faster solution from leetcode
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


def test(vals):
    s = Solution()
    for v in vals:
        res = s.groupAnagrams2(v[0])
        print(
            v,
            ' -> ',
            Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        )
        print(Style.RESET_ALL, end='')


if __name__ == '__main__':
    vals = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        (["a"], [['a']]),    
        ([""], [[""]])
    ]

    test(vals)