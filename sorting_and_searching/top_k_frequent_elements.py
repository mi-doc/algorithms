import random
import heapq
from typing import List
from collections import Counter

# The essence of the task
TASK = """
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""


class Solution:
    """

    """
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """
        My solution
        """
        return [e for (e, n) in Counter(nums).most_common()[:k]]


    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        Proper solution from leetcode.
        """
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        """
        Solution from youtube. Using bucketsort. O(n) time.
        """
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        """
        Using min heap. O(n*logk)
        """
        h = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, freq in count.items():
            if len(h) == k:
                heapq.heappushpop(h, (freq, num))
            else:
                heapq.heappush(h, (freq, num))
        
        # Shorter alternative:
        # return heapq.nlargest(k, count.keys(), key=count.get)
        return [num for freq, num in h]

        
