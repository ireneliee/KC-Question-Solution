
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n < 2:
            return [0, 1]
        if n == 1:
            return [0]
        adj_list = dict()

        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            node_1 = edge[0]
            node_2 = edge[1]

            adj_list[node_1].append(node_2)
            adj_list[node_2].append(node_1)
        
        print(adj_list)

        leaves = []
        for node in adj_list:
            if len(adj_list[node]) == 1:
                leaves.append(node)
        
        while n > 2:
            n = n - len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves

        
sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(sol.findMinHeightTrees(n, edges))