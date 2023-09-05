# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        result = []

        def inorder_traversal(root):
            if root == None:
                return
            print('Appending root.val ' + str(root.val))
            
            inorder_traversal(root.left)
            result.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)
        print(result)
        return result[k - 1]

three = TreeNode(3)
one = TreeNode(1)
four = TreeNode(4)
two = TreeNode(2)

three.left = one
three.right = four
one.right = two

s = Solution()
print(s.kthSmallest(one, 1))