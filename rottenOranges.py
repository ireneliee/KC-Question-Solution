from collections import deque

class Solution(object):
    def isOnGrid(self,r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        time = -1
        fresh = 0
        
        rotten = deque()
        
        for r in range(n):
            for c in range(m):
                val = grid[r][c]
                if val == 2:
                    rotten.append((r, c))
                elif val == 1:
                    fresh += 1
                    
        if not fresh:
            return 0
        
        while rotten:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for newR, newC in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if self.isOnGrid(newR, newC, grid) and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        rotten.append((newR, newC))
                        fresh -= 1
            time += 1
                        
        if fresh:
            return -1
        return time
        