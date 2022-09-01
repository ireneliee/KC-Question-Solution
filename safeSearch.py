class TrieNode:
      
    # Trie node clas
    def __init__(self):
        self.children = [None]*26

  
class Trie:
      
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
      
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
          
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
          
        return ord(ch)-ord('a')
  
  
    def insert(self,key):
          
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

  
    def search(self, key):
          
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        return True
    
def checkQueries(keywords, unsafeWords, queries):
    result = []
    def keywordExist(vocab):
        return keyword_trie.search(vocab)
    def keywordUnsafe(vocab):
        return unsafeWord_trie.search(vocab)
    
    def process(vocab):
        keyword_exist = keywordExist(vocab)
        keyword_unsafe = keywordUnsafe(vocab)
        if not keyword_exist:
            return 0
        else:
            if keyword_unsafe:
                return -1
            else:
                return 1
    keyword_trie = Trie()
    for item in keywords:
        keyword_trie.insert(item)
    
    unsafeWord_trie = Trie()
    for item in unsafeWords:
        unsafeWord_trie.insert(item)
    
    for word in queries:
        result.append(process[word])
    
    return result
    
    

safeWord = ["bird", "flop", "turtle", "camping"]
unsafeWord = ["camp", "slytherin", "flipflop"]
queries = ["campi", "fl", "flip", "flop", "b"]
print(checkQueries(safeWord, unsafeWord, queries))
    