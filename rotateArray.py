import copy
class Solution(object):
    def rotate(self, nums, k):
        fullArray = nums + nums

        n = len(nums)

        return fullArray[(n - k):(2 * n - k)]

s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(s.rotate(nums, k))
        