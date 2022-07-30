
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = []
        visited = []

        for i in range(len(mat)):
            result.append([])
            visited.append([])
            for j in range(len(mat[i])):
                result[i].append(None)
                visited[i].append(False)


        def find_zero(i:int, j:int) -> List[int]:
            print(' i is ' + str(i))
            print(' j is ' + str(j))
            if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
                return 214748364
            else:
                visited[i][j] = True
            
                if mat[i][j] == 0:
                    return 0
                else:
                    a = 2147483647
                    b = 2147483647
                    c = 2147483647
                    d = 2147483647

                    if i + 1 < len(mat):
                        if visited[i + 1][j] == False:
                            a = find_zero(i + 1, j)
                        else:
                            a = mat[i + 1][j]
                    if i - 1 >= 0:
                        if visited[i - 1][j] == False:
                            b = find_zero( i - 1, j)
                        else:
                            b = mat[i - 1][j]
                    if j + 1 < len(mat[0]):
                        if visited[i][j + 1] == False:
                            c = find_zero(i, j + 1)
                        else:
                            c = mat[i][j + 1]
                    if j - 1 >= 0:
                        if visited[i][j - 1] == False:
                            d = find_zero(i, j -1)
                        else:
                            d = mat[i][j-1]

                    return min(a, b, c, d) + 1

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    visited[i][j] = True
                else:
                    result[i][j] = find_zero(i,j)

        return result
        
sol = Solution()
mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
print(sol.updateMatrix(mat))