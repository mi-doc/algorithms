from typing import List

# The essence of the task
TASK = """

"""


class Solution:
    """

    """
    def canJump(self, nums: List[int]) -> bool:
        """
        Dynamic programming solution.
        Time: O(n^2)
        """
        s = [0]
        visited = set()
        while s:
            i = s.pop()
            visited.add(i)
            if i == len(nums) - 1:
                return True
            
            for n in range(nums[i]):
                jump = i + n + 1
                if jump < len(nums) and jump not in visited:
                    s.append(jump)
        
        return False

    def canJump2(self, nums: List[int]) -> bool:
        """
        'Gready' solution.
        Time: O(n)
        """
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0