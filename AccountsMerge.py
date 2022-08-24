from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # list of nodes
        nodes = set()
        # hashmap mapping the email owner & email
        email_dict = {}
        # adjacency list to store the graph
        adjacency_list = {}
        
        # setting up the adjacency lsit
        for i in range(len(accounts)):
            account_owner = accounts[i][0]
            email_list = accounts[i][1:]
            
            for j in range(len(email_list)):
                nodes.add(email_list[j])
                if email_list[j] not in adjacency_list:
                    email_dict[email_list[j]] = account_owner
                    all_email_without_one = email_list.copy()
                    all_email_without_one.remove(email_list[j])
                    adjacency_list[email_list[j]] = set(all_email_without_one)
                    
                else:
                    all_email_without_one = email_list.copy()
                    all_email_without_one.remove(email_list[j])
                    curr_set_email = set(all_email_without_one)
                    adjacency_list[email_list[j]] = adjacency_list[email_list[j]].union(curr_set_email)
        
        
        list_of_nodes = list(nodes)
        visited = {}
        #setting up visited hashmap
        for i in range(len(list_of_nodes)):
            visited[list_of_nodes[i]] = False

        result = []
        full_email_list = []

        def dfs(node):
            if visited[node] == False:
                full_email_list.append(node)
                visited[node] = True
                set_of_neighbors = adjacency_list[node]
                for item in set_of_neighbors:
                    dfs(item)
                    

        
        

        for item in nodes:
            if visited[item] == False:
                dfs(item)
                full_email_list.sort()
                full_email_list = [email_dict[item]] + full_email_list
                result.append(full_email_list)
                full_email_list = []

                    
        return result

sol = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(sol.accountsMerge(accounts))
                    
