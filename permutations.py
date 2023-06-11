import copy

class Solution(object):
    def permute(self, nums):
        len_nums = len(nums)

        result = []

        def find(currList, total):
            if currList and total == len_nums:
                result.append(currList)
            else:
                for item in nums:
                    if item not in currList:
                        deep_copy = currList[:]
                        deep_copy.append(item)

                        find(deep_copy, total + 1)
        
        find([], 0)
        
        return result

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s = Solution()
nums = [1]
print(s.permute(nums))

            