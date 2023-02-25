from typing import List

# The essence of the task
TASK = """
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""


class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        is_col = False
        
        for r in range(R):
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
                    
        for r in range(R-1,-1,-1):
            for c in range(1, C):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
            if is_col:
                matrix[r][0] = 0
        