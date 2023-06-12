class Solution(object):
    def merge(self, intervals):
        result = []
        interval_len = len(intervals)


        
        counter = 0

        start = intervals[0][0]
        end = intervals[0][1]

        while counter < interval_len:
            curr = intervals[counter]
            start = min(start, curr[0])
            end = max(end, curr[1])

            if counter == interval_len - 1:
                result.append([start,end])
                break

            if end < intervals[counter + 1][0]:
                result.append([start, end])
                start = intervals[counter + 1][0]
                end = intervals[counter + 1][1]
    
            counter = counter + 1
        
        return result


        

s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))