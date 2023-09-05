class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        result = []
        visit, cycle = set(), set()

        courses_dict = { i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses_dict[course].append(prereq)

        def dfs(crs):
            if crs in cycle:
                return False
            elif crs in visit:
                return True
            
            cycle.add(crs)
            for pre in courses_dict[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        
        
        return result
       
            
        

numCourses = 2
prereq = [[1,0]]
s = Solution()
print(s.findOrder(numCourses, prereq))