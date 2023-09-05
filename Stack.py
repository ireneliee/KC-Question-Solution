from collections import deque
class Stack:
    def __init__(self):
        self.train = deque() 
        self.maxstack = deque()

    def push(self, animal):
        self.train.append(animal)

        if (len(self.maxstack) == 0 or self.maxstack[-1] < animal):
            self.maxstack.append(animal)
        else:
            self.maxstack.append(self.maxstack[-1])
    
    def pop(self):
        if len(self.train) < 1:
            return None

        self.train.pop()
        self.maxstack.pop()
    
    def is_empty(self):
        if len(self.train < 1):
            return True
        else:
            return False
    
    def print_stack(self):
        stack_temp = "[bottom]"
        for compartment in self.train:
            stack_temp = stack_temp + str(compartment) + "-->"
        
        stack_temp = stack_temp + "[top]"
        return stack_temp
    
    def get_max(self):
        return self.maxstack[-1] # O(1)


aidan_train = Stack()
aidan_train.push(1)
aidan_train.push(4)
aidan_train.push(2)
aidan_train.push(7)

print(aidan_train.get_max())




