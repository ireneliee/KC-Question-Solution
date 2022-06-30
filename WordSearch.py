from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return False
        
        x_coor = [-1,0,0,1]
        y_coor = [0,-1,1,0]
        
        def backtrack(x, y, history, word_left):
            result = False
            if len(word_left) == 0:
                return True
            history.append((x,y))
            
            #check if there's somewhere you can go
            next = word_left[0]
            for i in range(len(x_coor)):
                go_to_x = x + x_coor[i]
                go_to_y = y + y_coor[i]
                print('(' + str(go_to_x) + ',' + str(go_to_y) + ')')

                if (0 <= go_to_x < len(board)) and (0 <= go_to_y <len(board[go_to_x])) and (board[go_to_x][go_to_y] == next) and (history.count((go_to_x,go_to_y)) == 0):
                    print('reach here')
                    print(word_left[1:])
                    result = backtrack(go_to_x, go_to_y, history, word_left[1:])

            return result  

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    #print('visiting x: ' + str(i) + ' y: ' + str(j))
                    if(backtrack(i, j, [], word[1:])):
                        return True
        
        return False

        

sol = Solution()
test_case_1 = [["C","A","A"],["A","A","A"],["B","C","D"]]
test_case_2 = "AAB"

print(sol.exist(test_case_1, test_case_2))