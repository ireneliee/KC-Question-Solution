# how?
# rules: basically all the word must be represented in 
# the word dict 
# return false if any not represented
# problem -> it's fine if not all is used 

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for item in wordDict:
                if i + len(item) <= len(s) and s[i:(i + len(item))] == item:
                    dp[i] = dp[i + len(item)]
                
                if dp[i]:
                    break
        
        return dp[0]

s = Solution()
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
print(s.wordBreak(word, wordDict))