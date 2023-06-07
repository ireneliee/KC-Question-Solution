import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        pool = set()

        def getCombi(currSum, numbers):
            
            if currSum == target:
                tupled = tuple(numbers)
                if tupled not in pool:
                    pool.add(tupled)
            elif currSum > target:
                return
            else:
                for item in candidates:
                    deep_copy = copy.deepcopy(numbers)
                    deep_copy.append(item)

                    getCombi(currSum + item, deep_copy)

