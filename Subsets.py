import copy

class Solution:
    def subsets(self, arr):
        result = []
        result.append([])
        n = len(arr)
        def add(curr, last_i):
            if last_i >= n:
                return
            
            print('Curr is ' + str(curr))
            print('Curr last_ i number is ' + str(arr[last_i]))
            deep_copy = copy.deepcopy(curr)
            deep_copy.append(arr[last_i])
            result.append(deep_copy)
            print('Adding deep copy ' + str(deep_copy))

            for i in range(last_i + 1, n):
                add(deep_copy, i)
        
        for i in range(len(arr)):
            add([], i)
        return result

solution = Solution()

# test case
nums = [1,2,3]

print(solution.subsets(nums))
