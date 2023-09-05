from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0

        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] > prices[buy]:
                maxProfit = max(maxProfit, prices[i] - prices[buy])
        return maxProfit

prices = [1,1,1,1,1,1,3,3]
sol = Solution()
print(sol.maxProfit(prices))