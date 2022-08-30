class Solution:
    def reverse(self, x: int) -> int:
        xx = ''
        x = str(x)
        if x.startswith('-'):
            xx = '-'
        for i in range(-1, -len(x)-1, -1):
            if x[i] == '-':
                continue
            xx += x[i]

        xx = int(xx)
        if xx > 2**31-1 or xx < -2**31:
            return 0

        return xx


if __name__ == '__main__':
    s = Solution()
    num = 153423646
    res = s.reverse(num)
    print(res)