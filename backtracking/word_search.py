from typing import List, Optional, Tuple

# The essence of the task
TASK = """
Given an m x n grid of characters board and a string word, 
return true if word exists in the grid. The word can be constructed from letters 
of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""


class Solution:
    """

    """
    def exist_recursive(self, board: List[List[str]], word: str) -> bool:
        """
        The solution wasn't accepted by leetcode: time limit exceeded.
        """
        def backtrack(path: List[tuple[int, int]] = []) -> bool:
            if len(path) == len(word):
                # If it is the last letter - the word has been found
                return True
            
            if not path:
                # Looking for the first letter
                for i, row in enumerate(board):
                    for j, letter in enumerate(row):
                        if letter == word[0] and backtrack([(i, j)]):
                            return True
            
            else:
                i, j = path[-1]
                # Now check neighboring cells without going beyond the borders
                for ii in (max(i-1, 0), min(i+1, len(board)-1)):
                    if board[ii][j] == word[len(path)] and not (ii,j) in path \
                        and backtrack(path + [(ii, j)]):
                            return True
                for jj in (max(j-1, 0), min(j+1, len(board[0])-1)):
                    if board[i][jj] == word[len(path)] and not (i,jj) in path \
                        and backtrack(path + [(i, jj)]):
                            return True

            return False
                        
        return backtrack()


    def exist_stack(self, board: List[List[str]], word: str) -> bool:
        """
        The solution wasn't accepted by leetcode: time limit exceeded.
        """
        stack = []
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter != word[0]:
                    continue
                stack.append([(i, j)])
        
        while stack:
            path = stack.pop()
            if len(path) == len(word):
                # If it is the last letter - the word has been found
                return True

            i, j = path[-1]
            # Now check neighboring cells without going beyond the borders
            for ii in (max(i-1, 0), min(i+1, len(board)-1)):
                if board[ii][j] == word[len(path)] and not (ii,j) in path:
                    stack.append(path + [(ii, j)])
            for jj in (max(j-1, 0), min(j+1, len(board[0])-1)):
                if board[i][jj] == word[len(path)] and not (i,jj) in path:
                    stack.append(path + [(i, jj)])
        
        return False

    def exist_dfs(self, board, word):
        """
        Solution from discussion on leetcode.
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
            or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res