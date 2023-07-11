class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n == 1:
            return s
        
        longest_palindrome = ""

        def isPalindrome(word):
            if word[::-1] == word:
                return True
            else:
                return False
            

            
        def findLongestPalindrome(start, end, curr_longest):
            if 0 <= start < n and 0 <= end <= n and start < end:
                print('Currently testing ' + s[start:end])
                if end - start > len(curr_longest) and isPalindrome(s[start:end]):
                    print('Current longest ' + str(s[start:end]))
                    curr_longest = s[start:end]
                    return findLongestPalindrome(start - 1, end + 1, curr_longest)
                else:
                        return curr_longest
            else:
                return curr_longest
        
        print('Searching odd')
        for i in range(1, n):
            print('Round ' + str(i))
            curr_longest = findLongestPalindrome(i, i + 1, "")
            if len(curr_longest) > len(longest_palindrome):
                longest_palindrome = curr_longest
        
        print('Searching even')
        for j in range(0, n):
            curr_longest = findLongestPalindrome(j, j + 2, "")
            if len(curr_longest) > len(longest_palindrome):
                longest_palindrome = curr_longest

        return longest_palindrome
        
s = Solution()
word = "cc"
print(s.longestPalindrome(word))