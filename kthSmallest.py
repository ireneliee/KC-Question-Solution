
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # find inorder traversal
        inor_list = []
        
        def inorder_traversal(node):
            if node is None:
                return 
            
            if node.left is not None:
                inorder_traversal(node.left)
                
            inor_list.append(node.val)
            
            if node.right is not None:
                inorder_traversal(node.right)
        
        inorder_traversal(root)
        print(inor_list)
        
        return inor_list[k - 1]
        