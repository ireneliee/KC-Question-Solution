class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):
 
    def insert(self, root, value):
         
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(value)
        elif value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases

        # Case 1 - Right Rotate
        if balance > 1 and value < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Left Rotate
        if balance < -1 and value > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right rotate
        if balance > 1 and value > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left rotate
        if balance < -1 and value < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root



    def leftRotate(self, node):
    
        print("rotating to the left on node ", node.val)
      
        tempRightChild = node.right
        t = tempRightChild.left

        tempRightChild.left = node 
        node.right = t

        # Update heights
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        tempRightChild.height = 1 + max(self.getHeight(tempRightChild.left),self.getHeight(tempRightChild.right))

        # Return the new root
        return tempRightChild

    def rightRotate(self, node):
        
        print("rotating to the right on node ", node.val)

        tempLeftChild = node.left 
        t = tempLeftChild.right  

        # Perform rotation
        tempLeftChild.right = node 
        node.left = t               

        # Update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        tempLeftChild.height = 1 + max(self.getHeight(tempLeftChild.left), self.getHeight(tempLeftChild.right))

        # Return the new root
        return tempLeftChild

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)