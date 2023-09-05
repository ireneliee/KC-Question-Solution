from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        list.sort(nums)
        print(str(nums[len(nums) - k]))
        return nums[len(nums) - k]
        