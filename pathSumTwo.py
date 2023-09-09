import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):

        
        result = []

        def recurse(currNode, currSum, arr):

            if not currNode:
                return

            currSum = currSum + currNode.val
            arr.append(currNode.val)
            
            if not currNode.left and not currNode.right:
                # leaf node
                if currSum == targetSum:
                    result.append(arr)
                
                return

            deep_copy1 = copy.deepcopy(arr)
            deep_copy2 = copy.deepcopy(arr)
            recurse(currNode.left, currSum, deep_copy1)
            recurse(currNode.right, currSum, deep_copy2)

        if root:
            recurse(root, 0, [])
        

        return result

s = Solution()
five = TreeNode(5)
four = TreeNode(4)
eight = TreeNode(8)

five.left = four
five.right = eight

eleven = TreeNode(11)
seven = TreeNode(7)
two = TreeNode(2)

four.left = eleven
eleven.left = seven
eleven.right = two 

eight.left = TreeNode(13)
four_ = TreeNode(4)
eight.right = four_
four_.left = TreeNode(5)
four_.right = TreeNode(1)



targetSum = 22
print(s.pathSum(five, targetSum))
        