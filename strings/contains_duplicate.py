class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        return len(s) != len(nums)
    
    def containsDuplicate2(self, nums):

        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False



if __name__ == '__main__':
    # arr = [1,2,3,4,4,5,6,7]
    # arr = [1,2,3,4,5]
    s = Solution()
    arr = [x for x in range(1_000)]
    import timeit

    print('Starting')
    number = 50
    # res = s.containsDuplicate(arr)
    res = timeit.timeit('res = s.containsDuplicate(arr)', globals=globals(), number=number)
    res2 = timeit.timeit('res = s.containsDuplicate2(arr)', globals=globals(), number=number)

    if res > res2:
        print(f"res2 is {res/res2} times faster")
    else:
        print(f"res is {res2/res} times faster")