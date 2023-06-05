from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        lenX = len(grid)
        lenY = len(grid[0])
        currentFreshOrange = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(lenY)] for _ in range(lenX)]

        bfs_q = deque()

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        def isOrange(x):
            if x != EMPTY:
                return True
            else:
                return False 

        for i in range(lenX):
            for j in range(lenY):
                if grid[i][j] == FRESH:
                        currentFreshOrange += 1
                elif grid[i][j] == ROTTEN:
                     bfs_q.append([i, j, 0])
        
        if currentFreshOrange == 0:
            return 0
        
        while bfs_q:
             popped = bfs_q.popleft()

             curr_x = popped[0]
             curr_y = popped[1]
             curr_time = popped[2]

             visited[curr_x][curr_y] = True

             if grid[curr_x][curr_y] == FRESH:
                grid[curr_x][curr_y] == ROTTEN
                currentFreshOrange = currentFreshOrange - 1

                if currentFreshOrange == 0:
                     return curr_time

             for direction in directions:
                  new_x = curr_x + direction[0]
                  new_y = curr_y + direction[1]

                  if 0 <= new_x < lenX and 0 <= new_y < lenY and isOrange(grid[new_x][new_y]) and not visited[new_x][new_y]:
                       bfs_q.append([new_x, new_y, curr_time + 1])
                       visited[new_x][new_y] = True
        
        return -1
            

s = Solution()
grid = [[0,2]]
print(str(s.orangesRotting(grid)))

        
        
        



        