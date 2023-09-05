class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    
s = Solution()
nums = [3,1,3,4,2]
print(s.findDuplicate(nums))

"""
This is a linked list problem. There will be a cycle inside the linked list, and we want to know what's the beginning of the cycle.
The arrow is represented by the index, eg:
nums = [1, 3, 4, 2, 2]
We'll have node 0 (beginning) pointing at node 3, because inside nums[0] is 1, and value at index 1 is 3.
Then node 3 will be pointing at node 2, because val at index 3 is 2.

Step 1: Use Floyd's to find the out the first index x the fast and slow pointer is intersected at
Step 2: Have another slow pointer, moving it together with the node resulted from step 1 (x). The place where they meet is the beginning of the cycle
"""