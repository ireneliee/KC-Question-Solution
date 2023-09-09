from collections import deque

class Solution(object):
    def decodeString(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append( int(k) * substr)  
        
        return "".join(stack)



s = Solution()
intp = "3[a2[c]]"
print(s.decodeString(intp))


        