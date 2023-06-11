import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        pool = set()
        candidates.sort()

        def getCombi(currSum, numbers):
            if currSum == target:
                numbers.sort()
                tupled = tuple(numbers)
                if tupled:
                    pool.add(tupled)
            elif currSum > target:                
                return
            else:
                for item in candidates:
                    deep_copy = copy.deepcopy(numbers)
                    deep_copy.append(item)
                    print('Curr sum is ' + str(currSum + item))
                    print('Deep copy is ' + str(deep_copy))
                    if currSum + item > target:
                        return
                    else:
                        getCombi(currSum + item, deep_copy)
        
        getCombi(0, [])

        answer = []

        for item_tuple in pool:
            answer.append(list(item_tuple))

        return answer
            
            

s = Solution()
candidates = [2,3,6,7]
target = 7

print(s.combinationSum(candidates, target))

# time limit exceeded -> some kind of cache would be ideal



