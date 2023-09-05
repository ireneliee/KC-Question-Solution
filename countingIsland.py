from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_mov = [0, 0, 1, -1]
        y_mov = [1, -1, 0, 0]
        
        visited = set()
        
        countIsland = 0
        
        def dfs(i, j):
            if (i, j) not in visited:
                visited.add((i, j))
                for k in range(len(x_mov)):
                    if 0 <= i + x_mov[k] < len(grid) and 0 <= j + y_mov[k] < len(grid[i]) and grid[i + x_mov[k]][j + y_mov[k]] == "1":
                        dfs(i + x_mov[k], j + y_mov[k])
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print('currently in i ' + str(i) + ' and j ' + str(j))
                if grid[i][j] == "1" and (i, j) not in visited:
                    print('i and j not in visited')
                    countIsland = countIsland + 1
                    dfs(i, j)
        
        return countIsland

sol = Solution()
island = [
  ["0"]
]
print(sol.numIslands(island))