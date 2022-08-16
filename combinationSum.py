
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates.sort()

        def helper(i: int, currTar: int, currList: List[int]):
            currSum = currTar - candidates[i]
            if currSum == 0:
                currList.append(candidates[i])
                result.append(currList)
                return
            elif currSum < 0:
                return
            else:
                currList.append(candidates[i])
                for k in range(i, len(candidates)):
                    helper(k, currSum, currList.copy())
        
        for i in range(len(candidates)):
            helper(i, target, [])

        return result
        
        

sol = Solution()
candidates = [2]
target = 1
print(sol.combinationSum(candidates, target))

        