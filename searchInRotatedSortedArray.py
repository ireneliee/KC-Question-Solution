from typing import List


class Solution:
    def search(self, nums, target) -> int:
        firstNum = nums[0]
        lastNum = nums[-1]

        lengthOfNus = len(nums)

    
        
        def findNumber():
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                print('Mid is ' + str(nums[mid]))
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    print('Target is smaller than mid')
                    if target >= firstNum:
                        print('Search to the left')
                        high = high - 1
                    else:
                        print('Search to the right')
                        low = low + 1 
                else:
                    print('Target is larger than mid')
                    if target < firstNum:
                        print('Search to the right')
                        low = low + 1
                    else:
                        print('Search to the right')
                        high = high - 1

            return -1 # not there bro
        
        indexInRotatedArray = findNumber()

        if indexInRotatedArray == -1:
            return -1
            
        
        print('------------------------')
        print('Index is ' + str(indexInRotatedArray))

        # orig + pivot + 1 = rigged

        return indexInRotatedArray
    
        


sol = Solution()
nums = [4,5,6,7,8,1,2,3]
target_index = sol.search(nums, 8)
print('Target index is ' + str(target_index))