from typing import List

# The essence of the task
TASK = """
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    """
    The key to this task is to sort the intervals list first,
    and then compare all consecutive intervals.
    Time: O(nlogn). Space: O(logn) because of sort.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1][-1] >= i[0]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
                
        return res