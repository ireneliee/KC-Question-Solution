# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def rightSideView(self, root):
        result = []

        level_node_dict = {}

        def traverse(node, currLevel):
            if not node:
                return
            if currLevel in level_node_dict:
                level_node_dict[currLevel].append(node.val)
            else:
                level_node_dict[currLevel] = [node.val]
        
            traverse(node.left, currLevel + 1)
            traverse(node.right, currLevel + 1)

        
        traverse(root, 1)

        print(level_node_dict)

        keys_ = list(level_node_dict.keys())

        for k in keys_:
            result.append(level_node_dict[k][-1])
        return result