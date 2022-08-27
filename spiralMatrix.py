from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        rowRecorded = 0

        result = []
        def goOneRound(step: int):
            # traverse to the right
            for i in range(0 + step, width - step):
                print('to the right')
                print('adding matrix ' + str(0 + step) + " " + str(i))
                result.append(matrix[0 + step][i])
                rowRecorded = 0 + step
            
            # traverse down
            for i in range(0 + 1 + step, height - step):
                print('to down')
                print('adding matrix ' + str(i) + " " + str(width - step - 1))
                result.append(matrix[i][width - step - 1])

            
            # traverse to the left
            for i in range(width - step - 2, 0 + step - 1, -1):
                print('to the left')
                print('adding matrix ' + str(height - step - 1) + " " + str(i))
                if rowRecorded == height-step-1:
                    break
                result.append(matrix[height - step - 1][i])
            
            # traverse up
            for i in range(height - step - 2, 0 + step, -1):
                print('to up')
                print('adding matrix ' + str(i) + " " + str(0 + step))
                result.append(matrix[i][0 + step])
        
        half = max(width, height) // 2 + 1
        for i in range(half):
            goOneRound(i)
        
        return result


sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))
