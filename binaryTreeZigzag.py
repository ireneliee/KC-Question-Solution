# binaryTreeZigzagLevelOrderTraversal
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        queue = []
        isLeft = True
        result = []

        line = []
        temp_queue = deque()

        queue.append(root)

        while len(queue) > 0:

            for i in range(len(queue)):
                node_now = queue.pop()
                line.append(node_now.val)
                
                if isLeft == False:
                    if node_now.right != None:
                        temp_queue.append(node_now.right)
                    if node_now.left != None:
                        temp_queue.append(node_now.left)
                else:
                    if node_now.left != None:
                        temp_queue.append(node_now.left)
                    if node_now.right != None:
                        temp_queue.append(node_now.right)
            
            #print(line)
            queue = temp_queue
            temp_queue = []
            result.append(line)
            line = []
            isLeft = not isLeft
            
        return result