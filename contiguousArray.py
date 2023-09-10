class Solution(object):
    def findMaxLength(self, nums):
        numDict = {}
        numDict[0] = [-1]
        currTotal = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                currTotal = currTotal - 1
            else:
                currTotal = currTotal + 1

            if currTotal in numDict:
                numDict[currTotal].append(i)
            else:
                numDict[currTotal] = [i]
        
        maxLength = 0

        for k in numDict:
            currIndexes = numDict[k]
            maxLength = max(maxLength, max(currIndexes) - min(currIndexes))
        
        return maxLength


s = Solution()
nums = [0, 1, 0, 0, 1, 1, 0, 0]
print(s.findMaxLength(nums))