from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        bracket_dict = {}
        bracket_dict['('] = ')'
        bracket_dict['{'] = '}'
        bracket_dict['['] = ']'

        for i in range(len(s)):
            x = s[i]
            print('current x is ' + x)
            if x == '(' or x == '[' or x =='{':
                stack.append(x)
                print('after stacking...' + x)
                print(str(stack))
                print('\n')
            elif x == ')' or x == ']' or x =='}':
                if stack:
                    y = stack.pop()
                    if bracket_dict[y] != x:
                        return False
                
                else:
                    return False

                print('after popping...' + y)
                print(str(stack))
                print('\n')

        if stack:
            return False

        return True
                
sol = Solution()
s = "(()))"
print(sol.isValid(s))
