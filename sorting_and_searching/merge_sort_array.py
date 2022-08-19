from typing import Optional, List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        
        temp = []
        i = k = t = 0
        while i < len(nums1):

            # We will use "temp" list to store all consequtive items from the nums1 list,
            # because when we meet a lower number in nums2 list, we will have to shift everything
            # in the nums1 to the right
            if temp and len(temp) > t:
                if i < m:
                    # Itmes with index more than 'm' are zeroes, so we don't need them
                    temp.append(nums1[i])
                if len(nums2) <= k or temp[t] <= nums2[k]:
                    nums1[i] = temp[t]
                    t += 1
                else:
                    nums1[i] = nums2[k]
                    k += 1
            
            # When we've gone through the nums1 list (i > m), and the temp list is empty,
            # we just add everything what's left in the nums2
            elif i >= m:
                nums1[i] = nums2[k]
                k += 1

            # If item from the second list is smaller, we assign it and put the bigger item
            # from the first list to the temp
            elif nums2[k] < nums1[i]:
                temp.append(nums1[i])
                nums1[i] = nums2[k]
                k += 1
            
            # If nums1 number smaller than from nums2, and no temp is present,
            # we just increment the index
            i += 1



def test(vals):
    s = Solution()
    for val in vals:
        s.merge(*val)
        print(val[0])


if __name__ == '__main__':
    vals = [
        [ [1,2,3,0,0,0], 3, [3,4,5], 3 ],
        [[3,4,5,6,0,0,0], 4, [1,2,9], 3],
        [[2,0], 1, [1], 1],
        [ [0], 0, [1], 1 ],
        [ [1], 1, [], 0],
        [ [2,5,6,0,0,0], 3, [2,5,9], 3]
    ]

    test(vals)