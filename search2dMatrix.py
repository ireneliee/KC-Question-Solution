from calendar import c
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(row_l, row_r, col_l, col_r):

            last_row_mid = 0
            last_col_mid = 0

            # print('Level 1...')
            while row_l <= row_r and col_l <= col_r:
                # print('row_l is ' + str(row_l))
                # print('row_r is ' + str(row_r))
                # print('col_l is ' + str(col_l))
                # print('col_r is ' + str(col_r))
                row_mid = (row_l + row_r) // 2
                col_mid = (col_l + col_r) // 2
                print('row mid is ' + str(row_mid))
                print('col mid is ' + str(col_mid))

                if matrix[row_mid][col_mid] == target:
                    print('reach here')
                    return True
                elif target > matrix[row_mid][col_mid]:
                    binarySearch(row_mid + 1, row_r, col_l, col_r)
                    binarySearch(row_l, row_r, col_mid + 1, col_r)
                else:
                    binarySearch(row_l, row_mid - 1, col_l, col_r)
                    binarySearch(row_l, row_r, col_l, col_mid - 1)
            return False

        return binarySearch(0, len(matrix), 0, len(matrix[0]))        
                
         
            # print('Level 2...')
            # while row_l <= row_r:
            #     row_mid = (row_l + row_r) // 2
                
            #     if matrix[row_mid][last_col_mid] == target:
            #         return True
            #     elif target > matrix[row_mid][last_col_mid]:
            #         binarySearch(row_mid + 1, row_r, col_l, col_r)
            #     else:
            #         binarySearch(row_l, row_mid - 1, col_l, col_r)
            
            # print('Level 3...')
            # while col_l <= col_r:
            #     col_mid = (col_l + col_r) // 2

            #     if matrix[last_row_mid][col_mid] == target:
            #         return True
            #     elif target > matrix[last_row_mid][col_mid]:
            #         binarySearch(row_l, row_r, col_mid + 1, col_r)
            #     else:
            #         binarySearch(row_l, row_r, col_l, col_mid - 1)

sol = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(sol.searchMatrix(matrix, target))

                
