import heapq
class Solution(object):
    def lengthOfLIS(self, nums):
        lis = [1 for _ in range(len(nums))]
        for x in range(len(nums) - 1, -1, -1):
            for y in range(x + 1, len(nums)):
                if nums[x] < nums[y]:
                    lis[x] = max(lis[x], lis[y] + 1)
        
        return max(lis)
                
s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))




