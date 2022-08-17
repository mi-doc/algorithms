from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    s = Solution()
    word = 'robat'
    anag = 'trabo'
    res = s.isAnagram(word, anag)
    print(res)