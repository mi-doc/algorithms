class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        sign = None
        s = s.lstrip()
        for c in s:
            if c in '-+' and not res and not sign:
                sign = int(c + '1')
                continue
            if not c.isdigit():
                break
            res += c
        if not res:
            return 0
        res = int(res) * (sign or 1)

        res = min(res, 2**31-1)
        res = max(res, -2**31)
        return res


if __name__ == '__main__':
    res = Solution()
    s = ' 4234299 bobba'
    # s = "3.14159"
    res = res.myAtoi(s)
    print(res)