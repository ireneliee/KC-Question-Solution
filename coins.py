def cashWithdraw(banknotes, amount):
    cache = {}
    len_banknotes = len(banknotes)
    cache[0] = 0
    
    for item in banknotes:
        for x in range(item, amount + 1):
            cache[x] = min(cache[x], cache[x - item] + 1)
    
    if amount not in cache:
        return -1
    else:
        return cache[amount]

banknotes = [1,2,5]
amount = 11
print(cashWithdraw(banknotes, amount))