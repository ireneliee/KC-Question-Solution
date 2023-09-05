

# Type your codes in the cell minimum cost to connect all paths.
# Create a function called minCostConnectPoints that takes in a 2d list points as parameter.
# 2.1. Create a list called list_of _points
# 2.2 Loop through the range of points given and append points[i][0] , points[i][1] into the list above
# 2.3 Create a new variable called source and assign item in first index of list_of_points
# 2.4 Create a new dictionary called adjacency_list
# 2.5 Loop through the length of points we have
# 2.5.1 Add the first point inside the adjacency list as the key and value as an empty list
# 2.5.2 Loop through the length of points we have again (Similar to bubble sort where we use 2 for loops to do comparison inside a list]
# 2.5.2.1 Check if list_of_points[i} != list_of_points[j]
# 2.5.2.2 Get the manhattan distance by calling the function provided and passing in the two points , then assigning it into a variable weight
# 2.5.2.3 Then add the list of points and weight into the adjacency list with the correct key
# 2.5.3 Return the results by passing adjacency_list and source into prim’s algorithm

# Create a function called minCostConnectPoints that takes in a 2d list points as parameter.

def prim(adjacency_list, source):
    priority_queue = {source : 0}
    added = set()
    minSpanTreeCost = 0

    while priority_queue:
        node = min(priority_queue, key = priority_queue.get)
        cost = priority_queue[node]

        del priority_queue[node]

        if node not in added:
            minSpanTreeCost += cost
            added.add(node)

            for edges in adjacency_list[node]:
                to_node = edges[0]
                weight = edges[1]
                if to_node in priority_queue.keys():
                    if priority_queue[to_node] > weight:
                        priority_queue[to_node] = weight
                else:
                    priority_queue[to_node] = weight


    return minSpanTreeCost

def get_manhattan_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1]- point2[1])

def minCostConnectPoints(points):
    # 2.1. Create a list called list_of _points
    list_of_points = []
    # 2.2 Loop through the range of points given and append points[i][0] , points[i][1] into the list above
    for i in range(len(points)):
        list_of_points.append((points[i][0],  points[i][1]))
    # 2.3 Create a new variable called source and assign item in first index of list_of_points
    source = list_of_points[0]
    # 2.4 Create a new dictionary called adjacency_list
    adjacency_list = {}
    # 2.5 Loop through the length of points we have
    for i in range(len(list_of_points)):
        # 2.5.1 Add the first point inside the adjacency list as the key and value as an empty list
        adjacency_list[list_of_points[i]] = []
        # 2.5.2 Loop through the length of points we have again (Similar to bubble sort where we use 2 for loops to do comparison inside a list]
        for j in range(len(list_of_points)):
            # 2.5.2.1 Check if list_of_points[i} != list_of_points[j]
            if list_of_points[i] != list_of_points[j]:
                # 2.5.2.2 Get the manhattan distance by calling the function provided and passing in the two points , then assigning it into a variable weight
                weight = get_manhattan_dist(list_of_points[i], list_of_points[j])
                # 2.5.2.3 Then add the list of points and weight into the adjacency list with the correct key
                adjacency_list[list_of_points[i]].append([list_of_points[j], weight])
    # 2.5.3 Return the results by passing adjacency_list and source into prim’s algorithm
    return prim(adjacency_list, source)

print(minCostConnectPoints([[3,12], [-2,5], [-4,1]]))








