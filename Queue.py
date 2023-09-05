from collections import deque

class Queue:
    def __init__(self):
        self.train = deque()

    def enqueue(self, animal):
        self.train.append(animal)
    
    def dequeue(self):
        if len(self.train < 1):
            return None
        self.train.popleft()
    
    def is_empty(self):
        return len(self.train) == 0
    
    def print_queue(self):
        queue_temp = "[Head]"
        for animal in self.train:
            queue_temp = queue_temp + str(animal) + "-->"
        queue_temp = queue_temp + "[tail]"
        print(queue_temp)

aidan_train = Queue()
aidan_train.enqueue("rabbit")
aidan_train.enqueue("zebra")
aidan_train.enqueue("wolf")
aidan_train.print_queue()