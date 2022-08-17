import math


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Creating sets with columns 
        cols = [set() for _ in range(len(board[0]))]

        # Calculating 3x3 squares on the field
        sqrs = []
        for _ in range (len(board)//3):
            sqrs.append([set() for _ in range(len(board)//3)])

        for i, r in enumerate(board):
            this_row = set()
            for j, c in enumerate(r):
                if c == '.':
                    continue
                # We have 3x3 squares and mast find out in which one we are currently in
                # to search for duplicates
                this_sqr = sqrs[math.floor(i//3)][math.floor(j//3)]
                if c in this_row or c in cols[j] or c in this_sqr:
                    return False
                this_row.add(c)
                cols[j].add(c)
                this_sqr.add(c)

        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        This was taken from a comment at leetcode
        """
        big = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i/3,j/3,cur))
        return True


if __name__ == '__main__':
    s = Solution()

    board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    # res = s.isValidSudoku2(board)
    # print(res)

    SPEED = 1


    if SPEED:
        import timeit
        # print('Creating list...')
        # arr = [x for x in range(1_000_0)]
        # print('Starting...')

        commands = [
            [ 'TASK-1', 's.isValidSudoku(board)', None ],
            [ 'TASK-2', 's.isValidSudoku2(board)', None ]
        ]

        for com in commands:
            com[2] = timeit.timeit(com[1], globals=globals(), number=500)


        sres = sorted(commands, key=lambda i: i[2])
        for i, c in enumerate(sres):
            if i == 0: 
                msg = f"{i+1} -> {c[0]} - ({round(100*float(c[2])/float(sres[1][2]))}% of {sres[1][0]} time)"
                continue
            msg += f"\n{i+1} -> {c[0]} is {round(c[2]/sres[0][2]*10)/10} times slower than {sres[0][0]}"

        print(msg)