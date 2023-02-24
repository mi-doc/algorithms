from typing import List
from collections import Counter

# The essence of the task
TASK = """
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.
"""


class Solution:
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_count = max(counts)
        max_count_items = counts.count(max_count)
        return max(len(tasks), (max_count-1) * (n+1) + max_count_items)
