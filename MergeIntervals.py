from heapq import heappop, heappush
from typing import List
from numpy import void


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = []
        result = []

        for i in range(len(intervals)):
            heappush(h , intervals[i])
        
        while h:
            curr = heappop(h)
            
            if len(h) != 0 and curr[1] >= h[0][0]:
                next = heappop(h)

                new_item = []
                new_item.append(min(curr[0], next[0]))
                new_item.append(max(curr[1], next[1]))
                heappush(h, new_item)
            else:
                result.append(curr)
        
        return result



intervals = [[1, 4], [4,5]]
sol = Solution()
print(sol.merge(intervals))