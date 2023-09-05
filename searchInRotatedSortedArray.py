from typing import List


class Solution:
    def search(self, nums, target):
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print('Mid is ' + str(nums[mid]))
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
                
        return -1   
            
            
        
        
    
        


sol = Solution()
nums = [4,5,6,7,0,1,2]
target_index = sol.search(nums,0 )
print('Target index is ' + str(target_index))