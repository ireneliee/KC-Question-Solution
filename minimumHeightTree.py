# convert to adjacency list -> easier to see parent-child relationship
# another dict
# calculate height for every node
# height storing in dict, height --> set()
# at the same time, keep track of the max height, so later can just retrieve

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        neighbors = [set() for x in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            temp = []

            for leaf in leaves:
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)

                    if len(neighbors[neighbor])==1:
                        temp.append(neighbor)
            
            leaves = temp
        
        return leaves

        # # converting to adjacency list
        # adjacency_list = {}
        # for i in range(n):
        #     adjacency_list[i] = []
        
        # for item in edges:
        #     from_node = item[0]
        #     to_node = item[1]

        #     adjacency_list[from_node].append(to_node)
        #     adjacency_list[to_node].append(from_node)

        # height_dict = {}
        # visited_array = n * [False]

        # def calculateHeight(currNode: int, visited_array: List[int], height_map) -> int:
        #     visited_array[currNode] = True
        #     if currNode in height_map:
        #         return height_map[currNode]
        #     else:
        #         neighbors = adjacency_list[currNode]
        #         all_been_visited = True
        #         for item in neighbors:
        #             if visited_array[item] == False:
        #                 all_been_visited = False
        #                 break
        #         if all_been_visited:
        #             height_map[currNode] = 1
        #         else:
        #             biggerHeight = 0
        #             for item in neighbors:
        #                 if visited_array[item] == False:
        #                     currHeight = calculateHeight(item, visited_array, height_map)
        #                     if currHeight > biggerHeight:
        #                         biggerHeight = currHeight
        #             height_map[currNode] = biggerHeight + 1
        #     print(height_map)
        #     return height_map[currNode]
        
    
        # for i in range(n):
        #     currHeight = calculateHeight(i, visited_array.copy(), {})
        #     if currHeight in height_dict:
        #         height_dict[currHeight].append(i)
        #     else:
        #         height_dict[currHeight] = [i]

        # minHeight = min(list(height_dict.keys()))
        # return height_dict[minHeight]


            
        
sol = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print(sol.findMinHeightTrees(n, edges))