from collections import deque
from typing import Optional 

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        # breadth first traversal
        
        queue = Deque()
        listOfNode = []
        
        queue.append(root)
        
        while queue:
            popped = queue.popleft()
            listOfNode.append(popped)
            if popped.left is not None:
                queue.append(popped.left)
            if popped.right is not None:
                queue.append(popped.right)
        
        # print(queue)
        # putting the next pointer
        m = 0
        count = 0
            
        for i in range(0, len(listOfNode)):
            count = count + 1
            if pow(2, m) == count or i == (len(listOfNode) - 1):
                count = 0
                m = m + 1
                listOfNode[i].next = None
            else:
                listOfNode[i].next = listOfNode[i + 1]
                
        return root