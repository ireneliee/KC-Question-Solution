from collections import deque 
class Solution(object):
    def dailyTemperatures(self, temperatures):
        output = [0 for i in range(len(temperatures))]
        stack = deque()

        for index in range(len(temperatures)):
            if stack and temperatures[index] >= stack[0][0]:
                while stack and temperatures[index] > stack[0][0]:
                    popped = stack.popleft()
                    diffInIndex = index - popped[1]
                    output[popped[1]] = diffInIndex
                
            stack.appendleft((temperatures[index], index))
        print(output)

s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
s.dailyTemperatures(temperatures)