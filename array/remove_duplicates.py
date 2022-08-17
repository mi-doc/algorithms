class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        gap = 1
        while i + gap < len(nums):
            if nums[i] == nums[i+gap]:
                gap += 1
                continue
            nums[i+1] = nums[i+gap]
            i += 1
        return i+1


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,3,4,4,5,6,7,7,8,8,8,8,9,10,11,11,11,11]
    res = s.removeDuplicates(nums)
    print(res, nums)
