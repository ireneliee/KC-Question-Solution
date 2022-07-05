from dataclasses import dataclass, field
from heapq import heappop, heappush, heapreplace
from typing import Any, List

    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        pq = []                         # list of entries arranged in a heap
        entry_finder = {}               # mapping of tasks to entries
        
        for i in range(len(nums)):
            if nums[i] in entry_finder:
                entry = entry_finder[nums[i]]
                count = entry[0]
                del(entry_finder[nums[i]])
                
            else:
                count = 0
            
            entry = [count + 1, nums[i]]
            entry_finder[nums[i]] = entry
        
            if pq:
                topmost_entry = pq[0]
                if count > topmost_entry[0]:
                    heapreplace(pq, entry)
            else:
                heappush(pq, entry)
        
        result = []
        
        for i in range(len(pq)):
            entry = heappop(pq)
            result.append(entry[i])
        
        return result

sol = Solution()

# test case
arr = [1,1,1,2,2,3]
k = 2

print(sol.topKFrequent(arr, k))