class Solution(object):
    def numIslands(self, grid):
        lenX = len(grid)
        lenY = len(grid[0])

        visited = [[False for _ in range(lenY)] for _ in range(lenX)]
        noOfIsland = 0

        def dfs(x, y):
            visited[x][y] = True

            directions = [(0, 1), (0, -1), (-1,0), (1, 0)]
            
            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if 0 <= newX < lenX and 0 <= newY < lenY and grid[newX][newY] == "1" and not visited[newX][newY]:
                    dfs(newX, newY)
        
        for x in range(lenX):
            for y in range(lenY):
                if grid[x][y] == "1" and not visited[x][y]:
                    noOfIsland = noOfIsland + 1
                    dfs(x, y)
        
        return noOfIsland
    

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))
                    
