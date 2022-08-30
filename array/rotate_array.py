class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if k > n:
            real_k = k
            k = n-1
            repeat = real_k // k
            kas = [k] * repeat
            kas.append(real_k % k)
        else:
            kas = [k]

        for k in kas:
            nums[:] = nums[n-k:]+nums[:n-k]

        return nums



if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,4,5,6,7]
    k = 13
    res = s.rotate(arr, k)
    print(res)
