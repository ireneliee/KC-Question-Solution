from typing import List

from numpy import true_divide


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currInd = len(nums) - 1

        while currInd > 0:
            if currInd - 1 >= 0 and nums[currInd - 1] + (currInd - 1) < currInd:
                return False
            else:
                currInd = currInd - 1
        
        return True

sol = Solution()
arr = [1,2]
print(sol.canJump(arr))
