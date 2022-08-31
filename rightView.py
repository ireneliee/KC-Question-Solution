class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        queue.appendleft(root)
        
        while queue:
            qLen = len(queue)
            level = []
            
            for i in range(qLen):
                x = queue.pop()
                if x:
                    level.append(x.val)
                    queue.appendleft(x.left)
                    queue.appendleft(x.right)
            
            levelLen = len(level)
            if levelLen == 0:
                break
            else:
                result.append(level[-1])
            
        
        return result