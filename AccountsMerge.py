class Node(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = set()

    def addEdge(self, neighbor):
        self.neighbors.add(neighbor)

class Solution(object):
    def accountsMerge(self, accounts):
        def dfs(start):
            list_of_graph_email = []
            stack = [start]  # Initialize stack with the starting vertex

            while stack:
                vertex = stack.pop()  # Get the next vertex from the stack

                if not visited_dict[vertex.val]:
                    list_of_graph_email.append(vertex.val)  # Process the vertex
                    visited_dict[vertex.val] = True

                    # Add unvisited neighbors of the current vertex to the stack
                    neighbors = vertex.neighbors
                    for neighbor in neighbors:
                        if not visited_dict[neighbor.val]:
                            stack.append(neighbor)
            
            return list_of_graph_email

        result = []
        
        email_node_dict = {}
        visited_dict = {}
        email_name_dict = {}

        # prep the graph
        for single_account in accounts:
            name = single_account[0]
            new_nodes = []

            for i in range(1, len(single_account)):
                email = single_account[i]
                if email in email_node_dict:
                    new_nodes.append(email_node_dict[email])
                else:
                    email_node = Node(email)
                    new_nodes.append(email_node)
                    email_node_dict[email] = email_node

                    email_name_dict[email] = name
            
            # connect the first node with the other nodes
            first_node = new_nodes[0]

            for i in range(1, len(new_nodes)):
                first_node.addEdge(new_nodes[i])

        # prep the visited_dict
        for email in email_node_dict:
            visited_dict[email] = False

        # visit all the nodes using dfs. If they have yet to be visited, dfs, and add the name and sorted list into result. Otherwise, ignore

        for email in email_node_dict:
            if not visited_dict[email]:
                email_list = dfs(email_node_dict[email])
                email_owner = email_name_dict[email]
                unique_account = [email_owner]

                email_list.sort()

                unique_account.extend(email_list)

                result.append(unique_account)


        return result

            
            
            
            


s = Solution()
accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
print(s.accountsMerge(accounts))
print(len(s.accountsMerge(accounts)))

