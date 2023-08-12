class Solution(object):
    def rob(self, nums):
        n = len(nums)
        # the max that you can get when you're in i, added is what {(i, added) => value}
        cache = {}
        def rob_house(i, totalSum, added):
            print('When i is ', str(i), ' and added is ', str(added))
            if i >= n:
                print('Terminate')
                return totalSum
            
            if (i, added) in cache:
                print('Retrieving from cache')
                return cache[(i, added)] + totalSum
            
            result = 0
            
            if added:
                result = rob_house(i + 1, totalSum, False)
            else:
                rob = rob_house(i + 1, totalSum + nums[i], True)
                not_rob = rob_house(i + 1, totalSum, False)
                
                result = max(rob, not_rob)

            cache[(i, added)] = result - totalSum
            print('Caching ',str((i, added)), ' as ', str((result)))
            return result
            
        
        return rob_house(0, 0, False)

s = Solution()
nums = [2,7,9,3,1]
print(s.rob(nums))
