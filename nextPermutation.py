class Solution(object):
    def nextPermutation(self, nums):
        # Find the first element that breaks the descending order from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If such element is found, find the smallest element to the right that is greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the elements to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums
        
s = Solution()
nums = [2,3,1,3,3]
print(s.nextPermutation(nums))