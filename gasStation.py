class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        if sum(gas) < sum(cost):
            return -1
        
        diff = []
        n = len(gas)

        for i in range(n):
            diff.append(gas[i] - cost[i])

        total = 0
        index = 0
        
        for i in range(n):
            before = total
            total = total + diff[i]
            if before == 0 and total > 0:
                index = i
            elif total < 0:
                total = 0
        
        return index
            


s = Solution()
gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))