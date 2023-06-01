from collections import deque

class MinStack(object):

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        self.height = 0
        

    def push(self, val):
        self.stack.append(val)
        if self.height == 0:
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[-1]
            if val > curr_min:
                self.min_stack.append(curr_min)
            else:
                self.min_stack.append(val)
        
        self.height = self.height + 1



    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        self.height = self.height - 1

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# [null,null,null,null,-3,null,0,-2]
        
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(str(minStack.getMin()))
minStack.pop()
print(str(minStack.top()))
print(str(minStack.getMin()))

