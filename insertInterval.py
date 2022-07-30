from typing import List
from urllib.parse import non_hierarchical


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        curr_start, curr_end = None, None
        for i in range(len(intervals)):
            if curr_start is None and curr_end is None:
                curr_start, curr_end = intervals[i][0], intervals[i][1]
            
            if i == len(intervals) - 1:
                result.append([curr_start, curr_end])
            else:
                next_start = intervals[i+1][0]
                next_end = intervals[i+1][1]

                if next_start <= curr_end:
                    curr_end = max([curr_end,next_end])
                else:
                    result.append([curr_start, curr_end])
                    curr_start = None
                    curr_end = None
        
        return result

sol = Solution()
intervals = [[1,7]]
newInterval = [4,8]
print(sol.insert(intervals, newInterval))