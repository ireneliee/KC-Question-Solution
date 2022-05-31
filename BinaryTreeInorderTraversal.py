
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        if root is None:
            return result;
        
        
        def traverse(root: Optional[TreeNode], result: List[int]):
            
            if root.left is not None:
                traverse(root.left, result)
            
            result.append(root.val)
            
            if root.right is not None:
                traverse(root.right, result)
        
        traverse(root, result)
        
        return result