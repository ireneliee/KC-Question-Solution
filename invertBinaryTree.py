from operator import invert
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invertTreeHelper(currNode):
            temp = TreeNode()

            if currNode.left is None and currNode.right is None:
                return currNode
            else:
                temp = currNode.left
                currNode.left = currNode.right
                currNode.right = temp

                if currNode.left is not None:
                     invertTreeHelper(currNode.left)
                
                if currNode.right is not None:
                    invertTreeHelper(currNode.right)
                
                return currNode

        root = invertTreeHelper(root)
        return root



