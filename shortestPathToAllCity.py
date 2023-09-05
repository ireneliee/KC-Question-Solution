# Add your codes in the cell Shortest Path to All Cities

# Type your codes in the cell shortest path to all cities
# Create a function find_shortest_distance that takes in an integer n and a 2d list edge_list, and return an integer shortest_distance
# 2.1 Create a dictionary called adjacency list
# 2.2 Loop through the number of cities given and add a new key and an empty list as the value
# 2.3 Loop through the edges given and create 3 variables,
# 2.3.1 From_node = edge[0], to_node = edge[1] and weight = edge[2]
# 2.3.2 Append the key as from node and value as to_node and weight to the adjacency list
# 2.3.3 Append the key as to node and value as from_node and weight to the adjacency list
# 2.4. return the results by passing the adjacency list into prim’s function

# Create a function find_shortest_distance that takes in an integer n and a 2d list edge_list, and return an integer shortest_distance


def prim(adjacency_list):
        priorityQueue = { 0 : 0 }
        added = set()
        minSpanTreeCost = 0

        while priorityQueue:
            node = min (priorityQueue, key = priorityQueue.get)
            cost = priorityQueue[node]
            
            del priorityQueue[node]
            
            if node not in added:
                minSpanTreeCost +=cost
                added.add(node)

                for edges in adjacency_list[node]:
                    to_node = edges[0]
                    weight = edges[1]

                    if to_node in priorityQueue.keys():
                        currentWeightToNode = priorityQueue[to_node]
                        if currentWeightToNode > weight:
                            priorityQueue[to_node] = weight
                    else:
                        priorityQueue[to_node] = weight
                    
        return minSpanTreeCost

def find_shortest_distance(n, edges):
    # 2.1 Create a dictionary called adjacency list
    adjacency_list = {}

    # 2.2 Loop through the number of cities given and add a new key and an empty list as the value
    for i in range(n):
        adjacency_list[i] = []
    
    # 2.3 Loop through the edges given and create 3 variables,
    for edge in edges:
        # 2.3.1 From_node = edge[0], to_node = edge[1] and weight = edge[2]
        from_node = edge[0]
        to_node = edge[1]
        weight = edge[2]

        # 2.3.2 Append the key as from node and value as to_node and weight to the adjacency list
        adjacency_list[from_node].append([to_node, weight])
        # 2.3.3 Append the key as to node and value as from_node and weight to the adjacency list
        adjacency_list[to_node].append([from_node, weight])

        # 2.4. return the results by passing the adjacency list into prim’s function
    


    return prim(adjacency_list)

print(find_shortest_distance(4, [[0,1,7], [0,3,6], [3,1,9], [3,2,8], [1,2,6]]))

