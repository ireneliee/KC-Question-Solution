
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def build(currentIndex: int) -> Optional[TreeNode]:
            
            newNode = None
            
            if visited[currentIndex] == False:
                newNode = TreeNode(preorder[currentIndex])
                # print('currently building ' + str(newNode.val))
                visited[currentIndex] = True
                
                inorderIndexOfCurr = nodeDict[preorder[currentIndex]]
                
                # find right child
                pointer = currentIndex
                while(pointer < len(preorder)):
                    
                    inorderIndexRight = nodeDict[preorder[pointer]]
                    
                    if inorderIndexRight > inorderIndexOfCurr:
                        # print('Building to the right')
                        newNode.right = build(pointer)
                        break
                    pointer = pointer + 1
                
                
                # find left child
                if currentIndex + 1 < len(preorder):
                    inorderIndexOfNext = nodeDict[preorder[currentIndex + 1]]
                    
                    if inorderIndexOfNext < inorderIndexOfCurr:
                        # print('Building to the left')
                        newNode.left = build(currentIndex+ 1)
                
               
                
            
            return newNode
                
            
        
        visited = [False for i in range(len(preorder))]
        
        nodeDict = {}
        
        for i in range(len(preorder)):
            nodeDict[inorder[i]] = i

        head = build(0)
        
        
        
        return head