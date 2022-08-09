class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        
class Trie:

    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:

        def insertUtil(root, value):
         
            if not root:
                return TreeNode(value)
            elif value < root.val:
                root.left = insertUtil(root.left, value)
            else:
                root.right = insertUtil(root.right, value)
    

            root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
    

            balance = self.getBalance(root)
    

            if balance > 1 and value < root.left.val:
                return self.rightRotate(root)
    

            if balance < -1 and value > root.right.val:
                return self.leftRotate(root)
    

            if balance > 1 and value > root.left.val:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
    

            if balance < -1 and value < root.right.val:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        
            return root

        self.root = insertUtil(self.root, word)

    def leftRotate(self, node):
    
        print("rotating to the left on node ", node.val)
      
        tempRightChild = node.right
        t = tempRightChild.left

        tempRightChild.left = node 
        node.right = t


        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        tempRightChild.height = 1 + max(self.getHeight(tempRightChild.left),self.getHeight(tempRightChild.right))


        return tempRightChild

    def rightRotate(self, node):
        
        print("rotating to the right on node ", node.val)

        tempLeftChild = node.left 
        t = tempLeftChild.right  


        tempLeftChild.right = node 
        node.left = t               


        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        tempLeftChild.height = 1 + max(self.getHeight(tempLeftChild.left), self.getHeight(tempLeftChild.right))


        return tempLeftChild

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height    

    def search(self, word: str) -> bool:
        def searchUtil(node, word):
            if node.val == word:
                return True
            elif word > node.val:
                if node.right is not None:
                    return searchUtil(node.right, word)
                else:
                    return False
            else:
                if node.left is not None:
                    return searchUtil(node.left, word)
                else:
                    return False
        
        return searchUtil(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def startsWithUtil(node: TreeNode, prefix: str) -> bool:
            prefix_len = len(prefix)

            if node.val[:prefix_len] == prefix:
                return True
            elif prefix > node.val[:prefix_len]:
                if node.right is not None:
                    return startsWithUtil(node.right, prefix)
                else:
                    return False
            else:
                if node.left is not None:
                    return startsWithUtil(node.left, prefix)
                else:
                    return False

        return startsWithUtil(self.root, prefix)


    def preOrder(self):
        
        def preOrderUtil(root):
            if not root:
                return
            print("{0} ".format(root.val), end="")
            preOrderUtil(root.left)
            preOrderUtil(root.right)
        
        preOrderUtil(self.root)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)