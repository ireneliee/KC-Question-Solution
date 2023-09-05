import copy

class Solution(object):
    def exist(self, board, word):

        x = [0, 1, -1, 0]
        y = [1, 0, 0, -1]

        m = len(board)
        n = len(board[0])

        cache = {}

        def visit(i, j, currIndex, visitedSet):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if board[i][j] != word[currIndex]:
                return False
            if (i, j, currIndex) in cache:
                return cache[(i, j, currIndex)]
            if (i, j) in visitedSet:
                return False
            if board[i][j] == word[currIndex] and currIndex == len(word) - 1:
                print('Fall here')
                return True
            
            currIndex = currIndex + 1

            visited_set_copy = copy.deepcopy(visitedSet)
            visited_set_copy.add((i, j))

            for index in range(4):
                result = visit(x[index] + i, y[index] + j, currIndex, visited_set_copy)
                cache[(x[index] + i, y[index] + j, currIndex)] = result
                if result:
                    return True
            
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if visit(i, j, 0, set()):
                        return True
        
        return False
            
     

sol = Solution()
test_case_1 = [["b","b","b","a","b","b"],["b","a","b","b","a","a"],["b","a","b","a","a","a"],["a","a","a","a","b","a"],["a","a","b","b","b","a"],["a","a","b","b","a","a"]]
test_case_2 = "abbbbaabbbbb"


print(sol.exist(test_case_1, test_case_2))
print(len(test_case_2))