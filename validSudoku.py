class Solution(object):
    def isValidSudoku(self, board):
        check_set = set()

        # check horizontal
        for i in range(9):
            check_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in check_set:
                    return False
                else:
                    check_set.add(board[i][j])
        
        # check vertical
        for j in range(9):
            check_set = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in check_set:
                    return False
                else:
                    check_set.add(board[i][j])

        # check 3 x 3 box
        it_list = [0, 3, 6]
        small_list = [0, 1, 2]
        for x in it_list:
            for y in it_list:
                check_set = set()
                for i in small_list:
                    for j in small_list:
                        currNum = board[x + i][y + j]
                        if currNum != "." and currNum in check_set:
                            return False
                        else:
                            check_set.add(currNum)
        
        return True
    

s = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))


