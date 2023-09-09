class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set()
        currTotal = 0

        for item in nums:
            num_set.add(item)

        for item in nums:
            if (item - 1) not in num_set:
                total = 1
                searching = item + 1

                while searching in num_set:
                    total = total + 1
                    searching = searching + 1
                
                currTotal = max(total, currTotal)
        
        return currTotal


s = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(s.longestConsecutive(nums))