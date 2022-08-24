from turtle import left
from typing import List, Set


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total / 2
        
        result_set = set()
        result_set.add(0)

        for i in range(len(nums) - 1, -1, -1):
            cop = list(result_set)

            for item in cop:
                result_set.add(item + nums[i])
            if half in result_set:
                return True
        
        return False

        

        
            
            

sol = Solution()
nums = [1,3,5,11]
print(sol.canPartition(nums))
