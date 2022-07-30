class Solution:
    def isPalindrome(self, s: str) -> bool:
        ori = ""
        for i in range(len(s)):
            curr = s[i].lower()
            if 97 <= ord(curr) <= 122 or 48 <= ord(curr) <= 57:
                ori = ori + curr



        for i in range(len(ori)):
            if ori[i] != ori[len(ori)- 1 - i]:
                return False
        return True

sol = Solution()
word = "race a car"
print(sol.isPalindrome(word))

