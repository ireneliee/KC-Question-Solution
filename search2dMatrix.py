from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(row_l, row_r, col_l, col_r) -> bool:

            while row_l <= row_r and col_l <= col_r:
                

                print('row_l is ' + str(row_l))
                print('row_r is ' + str(row_r))
                print('col_l is ' + str(col_l))
                print('col_r is ' + str(col_r))
                row_mid = (row_l + row_r) // 2
                col_mid = (col_l + col_r) // 2
                if row_mid >= len(matrix) or col_mid >= len(matrix[0]):
                    return False
                print('row mid is ' + str(row_mid))
                print('col mid is ' + str(col_mid))

                
                if matrix[row_mid][col_mid] == target:
                    print('reach here')
                    return True
                elif row_l == row_r and col_l == col_r:
                    print('broken')
                    return False
                elif target > matrix[row_mid][col_mid]:
                    print('target: '  + str(target)  + " is bigger than matrix " + str(matrix[row_mid][col_mid]))
                    if (binarySearch(row_mid + 1, row_r, col_l, col_r) or binarySearch(row_l, row_r, col_mid + 1, col_r)):
                        return True
                    else:
                        return False
                elif target < matrix[row_mid][col_mid]:
                    print('target: '  + str(target)  + " is smaller than matrix " + str(matrix[row_mid][col_mid]))
                    if binarySearch(row_l, row_mid - 1, col_l, col_r) or binarySearch(row_l, row_r, col_l, col_mid - 1):
                        return True
                    else:
                        return False
                else:
                    return False

            

        return binarySearch(0, len(matrix), 0, len(matrix[0]))        
            

sol = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(sol.searchMatrix(matrix, target))

                
