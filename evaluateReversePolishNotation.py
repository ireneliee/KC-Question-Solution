from typing import Deque, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = Deque()
        for i in range(len(tokens)):
            print('when token is '  + tokens[i])
            if tokens[i] == "+":
                b = num_stack.popleft()
                a = num_stack.popleft()
                result = int(a) + int(b)
                num_stack.appendleft(result)
            elif tokens[i] == "-":
                b = num_stack.popleft()
                a = num_stack.popleft()
                result = int(a) - int(b)
                num_stack.appendleft(result)
            elif tokens[i] == "/":
                b = num_stack.popleft()
                a = num_stack.popleft()
                result = int(int(a) / int(b))
                num_stack.appendleft(result)
            elif tokens[i] == "*":
                b = num_stack.popleft()
                a = num_stack.popleft()
                result = int(a) * int(b)
                num_stack.appendleft(result)
            else:
                num_stack.appendleft(tokens[i])

            print(str(num_stack))
        return num_stack.popleft()

sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))