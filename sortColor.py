class Solution(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        count2 = 0

        for item in nums:
            if item == 0:
                count0 = count0 + 1
            elif item == 1:
                count1 = count1 + 1
            elif item == 2:
                count2 = count2 + 1
        
        index = 0
        for i in range(count0):
            nums[index] = 0
            index = index + 1
        for i in range(count1):
            nums[index] = 1
            index = index + 1
        for i in range(count2):
            nums[index] = 2
            index = index + 1
        print('nums is ' + str(nums))
        

s = Solution()
arr = [2,0,1]
s.sortColors(arr)