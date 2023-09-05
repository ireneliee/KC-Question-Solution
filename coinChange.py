class Solution(object):
    def coinChange(self, coins, amount):

        cache = {}
        smallest_coin = min(coins)

        def findMinCoin(amount):
            print('Finding the min coins needed for amount ' + str(amount))

            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]
            
            if amount < smallest_coin:
                return -1

            min_coin = 2**31-1

            for coin in coins:
                print('Currently for coin ' + str(coin))
                curr_coin = findMinCoin(amount - coin)
                if curr_coin < min_coin and curr_coin != -1:
                    print('updating min coin to ' + str(curr_coin))
                    min_coin = curr_coin

            
            if min_coin != 2**31-1:
                cache[amount] = min_coin + 1
                return min_coin + 1
            else:
                cache[amount] = -1
                return -1
        
        print('Cache is ' + str(cache))
        
        return findMinCoin(amount)


coins = [261,411,27,78,61]
amount = 5456
s = Solution()
print(s.coinChange(coins, amount))