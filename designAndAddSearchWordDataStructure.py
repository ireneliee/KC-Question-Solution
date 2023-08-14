class TreeNode(object):
    def __init__(self, val):
        self.val = val
        # 'a' : TreeNode(a)
        self.children = {}
        self.isWord = False
    
    def __repr__(self):
        return f"TreeNode(val={self.val}, children={str(self.children)})"
    
class WordDictionary(object):

    def __init__(self):
        self.treeRoot = {}

    def addWord(self, word):
        currDict = self.treeRoot
        lastNode = None
        for i in range(len(word)):
            if word[i] in currDict:
                lastNode = currDict[word[i]]
            else:
                lastNode = TreeNode(word[i])
                currDict[word[i]] = lastNode
            currDict = lastNode.children
            
            if i == len(word) - 1:
                lastNode.isWord = True

    def search(self, word):
        print('Searching for word ', word)
        
        def search(currIndex, currDict, currNode):
            if currIndex >= len(word):
                if currNode.isWord:
                    return True
                else:
                    return False
            
            if word[currIndex] == ".":
                for item in currDict:
                    result = search(currIndex + 1, currDict[item].children, currDict[item])
                    if result:
                        return True
                return False
            else:
                if word[currIndex] not in currDict:
                    return False
                else:
                    return search(currIndex + 1, currDict[word[currIndex]].children, currDict[word[currIndex]])
        
        return search(0, self.treeRoot, None)


        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.treeRoot)
toSearch = ["pad", "bad", ".ad", "b.."]
for item in toSearch:
    print(obj.search(item))