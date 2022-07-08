from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binarySearch(l:int, r: int) -> int:
            if l == r:
                return l
            
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid + 1]:
                return binarySearch(l, mid)
            
            return binarySearch(mid + 1, r)
        
        return binarySearch(0, len(nums) - 1)
    

sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))