class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue

            tmp = currMax * n

            currMax = max(tmp, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax)

        return res

nums = [2,3,-2,4]
s = Solution()
print(s.maxProduct(nums))