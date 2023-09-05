class Solution(object):
    def productExceptSelf(self, nums):
        nums_len = len(nums)
        prefix_arr = []
        postfix_arr = []
        result = []

        prefix_arr.append(1)
        postfix_arr.append(1)

        for i in range(1, nums_len):
            prefix_arr.append(prefix_arr[i - 1] * nums[i - 1])
            postfix_arr.append(postfix_arr[i - 1] * nums[nums_len - i])
        
        for i in range(nums_len):
            result.append(prefix_arr[i] * postfix_arr[nums_len - i - 1])
        
        return result
    
s = Solution()
nums = [-1,1,0,-3,3]
print('result is ' + str(s.productExceptSelf(nums)))
            