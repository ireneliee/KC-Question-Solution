from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def recurse(index: int):
            if index >= len(nums):
                result.append(curr)
                return
            
            else:
                curr.append(nums[index])
                recurse(index + 1)
                curr.pop()
                recurse(index + 1)
        
        recurse(0)

        return result

solution = Solution()

# test case
nums = [1, 2, 3]

print(solution.subsets(nums))
