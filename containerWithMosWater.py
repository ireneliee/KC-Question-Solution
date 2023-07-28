class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        
        return res

            
                

s = Solution()
height = [1,2,1]
print(s.maxArea(height))