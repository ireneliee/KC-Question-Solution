from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binarySearch(start, end):
            if start == end:
                print('return ' + str(start))
                return start

            mid = (start + end) // 2
            print('when num is ' + str(nums[mid]))
            
        
            
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                print('left number is bigger than mid')
                binarySearch(start, mid)
            
            elif mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                print('right number is bigger than mid')
                binarySearch(mid, end)

        peak = binarySearch(0, len(nums) - 1)   
        return peak

sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))