# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n // 2 
        target = mid
        while True:
            mid = mid // 2
            if isBadVersion(target):
                if mid == 0:
                    while isBadVersion(target):
                        target -= 1
                    return target + 1
                target -= mid 
            else:
                if mid == 0:
                    while not isBadVersion(target):
                        target += 1
                    return target
                target += mid

    def firstBadVersion2(self, n) -> int:
        """
        Proper version from leetcode. It does 2x times less calls to "isBadVersion" function
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
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
        res = s.firstBadVersion2(val[0])
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