# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


def isBadVersion(n: int) -> bool:
    return n >= BAD_V


def test(vals):
    s = Solution()
    for val in vals:
        global BAD_V
        BAD_V = val[1]
        res = s.firstBadVersion(val[0])
        print(
            val,
            ' -> ',
            res == val[1],
            ' -> ',
            res
        )


if __name__ == '__main__':
    BAD_V = 0
    vals = [
        (5,4),
        [50,43],
        [3,2],
        [100,1],
        [17,16],
        [10,10],
        [1000, 580]
    ]

    test(vals)