class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


        return 'Not success'


if __name__ == '__main__':
    s = Solution()
    arr = [0, 1, 2, 3, 0, 4, 0, 0, 5, 6, 7, 0, 0, 0, 8, 9]

    SPEED = 0
    if not SPEED:
        res = s.twoSum(arr, 8)
        print(res)

    if SPEED:
        import timeit
        print('Preparing an array')
        # arrlen = 1_000_0
        # arr = [x for x in range(arrlen)]

        print('Starting')
        number = 500

        # res1 = timeit.timeit('res = s.twoSum(arr)', globals=globals(), number=number)

        # if res1 > res2:
        #     print(f"res2 is {round(res1/res2)} times faster ({round(100*float(res2)/float(res1))}% of res1 time)")
        # else:
        #     print(f"res1 is {round(res2/res1)} times faster ({round(100*float(res1)/float(res2))}% of res2 time)")