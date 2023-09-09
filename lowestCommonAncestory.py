class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None

        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node == p or node == q

            if (left and right) or (curr and left) or (curr and right):
                self.ans = node
                return
            
            return left or right or curr

        dfs(root)
        return self.ans


# three = TreeNode(3)
# five = TreeNode(5)
# one = TreeNode(1)
# six = TreeNode(6)
# two = TreeNode(2)
# seven = TreeNode(7)
# four = TreeNode(4)
# zero = TreeNode(0)
# eight = TreeNode(8)

# three.left = five
# five.left = six
# five.right = two
# two.left = seven
# two.right = four

# three.right = one
# one.left = zero
# one.right = eight

one = TreeNode(1)
two = TreeNode(2)

one.let = two

s = Solution()
node = s.lowestCommonAncestor(one, one, two)
print(node.val)