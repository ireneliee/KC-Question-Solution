from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates.sort()

        def helper(i: int, currTar: int, currList: List[int]):
            for i in range(i, len(candidates)):
                currSum = currTar - candidates[i]
                currList.append(currSum)
                if currSum == 0:
                    result.append(currList)
                    return
                elif currSum < 0:
                    return
                else:
                    helper(i + 1, currSum, currList.copy)
        
        helper(0, target, [])

        return result

sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target))

        