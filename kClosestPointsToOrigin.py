from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = []
        distance_points_dict = {}
        result = []

        for i in range(len(points)):
            calc = (points[i][0])**2 + (points[i][1])**2
            distance_list.append(calc)
            if calc in distance_points_dict:
                new = distance_points_dict[calc]
                new.append(points[i])
                distance_points_dict[calc] = new
            else:
                distance_points_dict[calc] = [points[i]]\
        
        distance_list.sort()
        n = 0
        i = 0
        while i < k and n < k :
            get_list = distance_points_dict[distance_list[i]]
            for j in range(len(get_list)):
                result.append(get_list[j])
                n = n + 1
            i = i  + 1
        return result

sol = Solution()
l = [[1,3],[-2,2]]
k = 1
print(sol.kClosest(l,k))

