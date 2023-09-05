from tkinter import N
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}

        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in result_dict:
                return [i, result_dict.get(num_to_find)]
            else:
                result_dict[nums[i]] = i

sol = Solution()
nums = [3,3]
target = 6

print(sol.twoSum(nums, target))