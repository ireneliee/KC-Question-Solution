from typing import List

from numpy import true_divide


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        def reachable(startInd, endInd):
            print('start index is ' + str(startInd))
            print('end index is ' + str(endInd))
            if endInd == 0:
                return True
            elif startInd < 0:
                return False
            elif startInd >= 0 and startInd + nums[startInd] >= endInd:
                return reachable(startInd - 1, startInd)
            elif startInd >= 0 and startInd + nums[startInd] < endInd:
                return reachable(startInd - 1, endInd)

        return reachable(len(nums) - 2, len(nums) - 1)   

sol = Solution()
arr = [2, 0, 0]
arr = [3,2,1,1,4]
print(sol.canJump(arr))
