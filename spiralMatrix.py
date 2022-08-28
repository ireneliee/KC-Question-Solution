from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        node_x = [0, 1, 0, -1]
        node_y = [1, 0, -1, 0]
        width = len(matrix[0])
        height = len(matrix)
        result = []
        visited = set()

        def dfs(i:int, j:int):
            visited.add((i, j))
            result.append(matrix[i][j])
            for x in range(4):
                if 0 <= i + node_x[x] < height and 0 <= j + node_y[x] < width:
                    if (i + node_x[x], j + node_y[x]) not in visited:
                        dfs(i + node_x[x], j + node_y[x])

        dfs(0, 0)
        return result

sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))
