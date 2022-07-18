from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_num = nums[0]
        last_num = nums[-1]


        def binarySearchPivotIndex(l, r):
            print('l is ' + str(l))
            print('r is ' + str(r))
            
            while l <= r:

                mid = (l + r) // 2

                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    return mid
                elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1] and nums[mid] >= first_num:
                    return binarySearchPivotIndex(mid + 1, r)
                elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1] and nums[mid] <= last_num:
                    return binarySearchPivotIndex(l, mid - 1)

            return -1
        
        pivotIndex = binarySearchPivotIndex(0, len(nums) - 1)
        
        def normalBinarySearch(arr, l, r):

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        left = nums[:pivotIndex + 1]
        right = []
        if pivotIndex != len(nums) - 1:
            right = nums[pivotIndex + 1 : ]
        # print('pivot index is ' + str(pivotIndex))
        # print('left is ' + str(left))
        # print('right is ' + str(right))
        left_target_index = normalBinarySearch(left, 0, len(left) - 1)
        # print('left target index is ' + str(left_target_index))
        right_target_index = normalBinarySearch(right, 0 , len(right) - 1)
        # print('right target index is ' + str(right_target_index))

        if left_target_index == -1 and right_target_index == -1:
            return -1
        elif left_target_index != -1:
            return left_target_index
        else:
            return len(left) + right_target_index


sol = Solution()
nums = [1,2,3,4,5,6,7]
target_index = sol.search(nums, 2)
print('Target index is ' + str(target_index))