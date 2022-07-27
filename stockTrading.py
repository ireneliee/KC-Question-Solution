from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0

        for i in range(len(prices)):
            print('when number is ' + str(prices[i]))
            if prices[i] < prices[buy]:
                print('changing buy to ' + str(prices[i]))
                buy = i
            elif prices[i] > prices[buy]:
                print('recalculating max profit')
                print('profit is ' + str(prices[i] - prices[buy]))
                maxProfit = max(maxProfit, prices[i] - prices[buy])
                print('maxProfit is ' + str(maxProfit))
        return maxProfit

prices = [1,1,1,1,1,1,3,3]
sol = Solution()
print(sol.maxProfit(prices))