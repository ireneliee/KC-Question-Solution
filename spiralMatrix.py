from typing import List

# not done yet but im bored af
class Solution:
    def spiralOrder(self, matrix):

        width = len(matrix[0])
        height = len(matrix)
        max_size = width * height
        result = []
        visited = []

        for i in range(height):
            visited.append([])
            for j in range(width):
                visited[i].append(False)

        def isNotValid(row, col):
            if row < 0 or row >= height or col < 0 or col >= width or visited[row][col]:
                return True
            else:
                return False
            
        # right, down, left, up
        node_x = [0, 1, 0, -1]
        node_y = [1, 0, -1, 0]

        
        def spiral(row, col, state, count):

            if count >= max_size:
                return
            
            result.append(matrix[row][col])
            visited[row][col] = True
            count = count + 1

            currState = state % 4
            nextState = (state + 1) % 4

            if isNotValid(row + node_x[currState], col + node_y[currState]):
                spiral(row + node_x[nextState], col + node_y[nextState], nextState, count)
            else:
                spiral(row + node_x[currState], col + node_y[currState], currState, count)

        spiral(0, 0, 0, 0)
        return result

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(sol.spiralOrder(matrix))