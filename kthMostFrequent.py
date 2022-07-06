from dataclasses import dataclass, field
from heapq import heapify, heappop, heappush, heapreplace
from typing import Any, List

    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        pq = []
        heapify(pq)                         # list of entries arranged in a heap
        entry_finder = {}               # mapping of tasks to entries
        
        for i in range(len(nums)):
            print('when nums is ' + str(nums[i]))
            if nums[i] in entry_finder:
                print('Can find the number inside dict')
                entry = entry_finder[nums[i]]
                count = entry[0]
                
            else:
                print('Cannot find the number inside dict')
                count = 0
            
            
            entry = [count - 1, nums[i]]
            print('Entry is ' + str(entry))
            entry_finder[nums[i]] = entry
        
            print('just pushing ' + str(entry))
            heappush(pq, entry)
        
        result = []
        rank = 0
        print(str(pq))
        while pq and rank < k:
            entry = heappop(pq)
            print('popped ' + str(entry))
            if entry[1] not in result:
                result.append(entry[1])
                rank = rank + 1
        
        return result

sol = Solution()

# test case
arr = [1,1,2,3,4,52,1,2,3,4]
k = 3

print(sol.topKFrequent(arr, k))