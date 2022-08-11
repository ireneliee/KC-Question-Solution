from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        
        def inOrderTraversal(node):
            if node.left is not None:
                inOrderTraversal(node.left)
                
            result.append(node.val)
            
            if node.right is not None:
                inOrderTraversal(node.right)
            
        inOrderTraversal(root)
        
        s = set(result)
        if len(s) != len(result):
            return False
        
        result_copy = result.copy()
        result.sort()
        
        return result == result_copy