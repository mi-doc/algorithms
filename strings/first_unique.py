class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = None
            else:
                d[c] = i

        return min((v for v in d.values() if v != None), default=-1)



if __name__ == '__main__':
    s = Solution()
    q = 'leetcode'
    res = s.firstUniqChar(q)
    print(res)