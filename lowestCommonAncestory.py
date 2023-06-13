class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        def findNumber(node, target):
            if node == None:
                return False
            if node == target:
                return True
            elif node.left == None and node.right == None:
                return False
            
            return findNumber(node.left, target) or findNumber(node.right, target)
        
        def findRoot(node):
            print('When node is ' + str(node.val))
            pIsLeft = False
            qIsLeft = False

            pIsLeft = findNumber(node.left, p)
            print('can find ' + str(p.val) + ' in left: ' + str(pIsLeft))
            qIsLeft = findNumber(node.left, q)
            print('can find ' + str(q.val) + ' in left: ' + str(qIsLeft))
            if pIsLeft != qIsLeft:
                return node

            if pIsLeft == qIsLeft:
                if node == p or node == q:
                    return node
                else:
                    if pIsLeft:
                        return findRoot(node.left)
                    else:
                        return findRoot(node.right)
                    
        return findRoot(root)
            


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