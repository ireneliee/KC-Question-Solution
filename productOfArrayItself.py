class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        
        
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i - 1] * nums[i])
                
        postfix = []
        postfix = [None] * len(nums)
        
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                postfix[j] = nums[j]
            else:
                postfix[j] = postfix[j + 1] * nums[j]
        
        print(prefix)
        print(postfix)
        
        result = []
        
        for k in range(len(nums)):
            if k == 0:
                result.append(postfix[k + 1])
            elif k == len(nums) - 1:
                result.append(prefix[k - 1])
            else:
                result.append(prefix[k - 1] * postfix[k + 1])
        
        return result