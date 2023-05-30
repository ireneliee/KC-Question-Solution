class Solution(object):
    def coinChange(self, coins, amount):

        
        min_coins_map = {}
        smallest_coin = min(coins)

        if amount == 0:
            return 0
        elif amount < smallest_coin:
            return -1

        for coin in coins:
            min_coins_map[coin] = 1

        def findMinCoins(target):
            print('Current target is '+ str(target))
            print(min_coins_map)

            stop = target // 2
            currMinCoins = 2**63-1

            for i in range(1, stop + 1):
                remaining = target - i

                if i < target and remaining < target and min_coins_map[i] != -1 and min_coins_map[remaining] != -1:
                    currMinCoins = min(currMinCoins, min_coins_map[i] + min_coins_map[remaining])
            
            if currMinCoins == 2**63-1:
                return -1
            else:
                return currMinCoins

        for target in range(0, amount + 1):
            if target < smallest_coin:
                min_coins_map[target] = -1
            
            elif target not in coins:
                min_coins_map[target] = findMinCoins(target)
        
        
        
        return min_coins_map[amount]


coins = [1,3,5]
amount = 11
s = Solution()
print(s.coinChange(coins, amount))