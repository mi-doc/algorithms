class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        This solution was copied from comments on leetcode. (sadly I didn't come up with my own)
        """
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]
    res = s.rotate(matrix)
    print(res == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    print(res)
