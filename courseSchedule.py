from concurrent.futures.process import _ThreadWakeup
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < numCourses:
            return False
        def isCycle(node, visited, recStack):
            visited[node] = True
            recStack[node] = True

            list_of_neighbors = []

            for i in range(len(prerequisites)):
                if prerequisites[i][1] == node:
                    list_of_neighbors.append(prerequisites[i][0])
            
            for i in range(len(list_of_neighbors)):
                if visited[i] == False:  
                    if isCycle(i, visited, recStack) == True:
                        return True
                elif recStack[i] == False:
                    return True
            
            recStack[node] = False
            return False

        
        visited = [False] * numCourses
        recStack = [False] * numCourses

        for i in range(numCourses):
            if visited[i] == False:
                if isCycle(i, visited, recStack) == True:
                    return False
        return True

sol = Solution()
prereq = [[1,0],[0,1]]
print(sol.canFinish(2, prereq))