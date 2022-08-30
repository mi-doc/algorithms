class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        sep = -1
        for i in range (-1, -len(nums)-1, -1):
            if nums[i] == 0:
                for k in range(i, sep):
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                sep -= 1

        return nums

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last0 = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                nums[i],nums[last0] = nums[last0],nums[i]
                last0+=1

        return nums

if __name__ == '__main__':
    s = Solution()
    arr = [0, 1, 2, 3, 0, 4, 0, 0, 5, 6, 7, 0, 0, 0, 8, 9]
    # arr = [x for x in range(1000)]
    arr = [0,1,0,3,12]

    SPEED = 1
    if not SPEED:
        res = s.moveZeroes2(arr)
        print(res)

    if SPEED:
        import timeit
        print('Preparing an array')
        arrlen = 1_000_0
        arr = [x for x in range(arrlen)]
        print('Inserting zeroes')
        for x in range(0, arrlen, 100):
            arr[x] = 0

        print('Starting')
        number = 500

        res1 = timeit.timeit('res = s.moveZeroes1(arr)', globals=globals(), number=number)
        res2 = timeit.timeit('res = s.moveZeroes2(arr)', globals=globals(), number=number)

        if res1 > res2:
            print(f"res2 is {round(res1/res2)} times faster ({round(100*float(res2)/float(res1))}% of res1 time)")
        else:
            print(f"res1 is {round(res2/res1)} times faster ({round(100*float(res1)/float(res2))}% of res2 time)")