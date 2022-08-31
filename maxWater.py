from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n - 1
        maxWater = 0

        while start < end and start < n and end >= 0:
            maxWater = max((min(height[start], height[end]) * (end - start)), maxWater)
            if height[start] <= height[end]:
                start = start + 1
            elif height[end] < height[start]:
                end = end - 1
        return maxWater


sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
            
            