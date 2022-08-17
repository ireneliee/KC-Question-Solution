from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permuteHelper(currList: List[int]):
            if len(currList) == len(nums):
                result.append(currList)
                print('current result is ' + str(result))
            else:
                
                for i in range(len(nums)):
                    if nums[i] not in currList:
                        print('appending ' + str(nums[i]) + ' to currlist' + str(currList))
                        currList.append(nums[i])
                        permuteHelper(currList.copy())
                        currList.pop()
        
            

        for i in range(len(nums)):
            permuteHelper([nums[i]])
        return result


sol = Solution()
nums = [1]
print(sol.permute(nums))
