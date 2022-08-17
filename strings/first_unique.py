class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = None
                continue
            d[c] = i


        return c



if __name__ == '__main__':
    s = Solution()
    q = 'fsdfweasdfwg'
    res = s.firstUniqChar(q)
    print(res)