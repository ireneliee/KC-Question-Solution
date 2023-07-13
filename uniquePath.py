class Solution:
    def uniquePaths(self, m, n):
        count_dict = {}
        def find(currM, currN):
            if (currM, currN) in count_dict:
                return count_dict[(currM, currN)]
            if currM >= m or currN >= n:
                return 0
            if currM == m - 1 and currN == n - 1:
                return 1
            
            currNoOfPath = find(currM + 1, currN) + find(currM, currN + 1)
            count_dict[(currM, currN)] = currNoOfPath
            return currNoOfPath
        
        return find(0, 0)
sol = Solution()
print(sol.uniquePaths(3, 7))