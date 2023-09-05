

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)
            
class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list
        
    def add_edge(self, node_1, node_2):
        
        if(node_1 in self.nodes and node_2 in self.nodes):
            node_1.add_child(node_2)
            node_2.add_child(node_1)

    def remove_edge(self, node_1, node_2):
        
        if(node_1 in self.nodes and node_2 in self.nodes):
            node_1.remove_child(node_2)
            node_2.remove_child(node_1)
    
    def dfs(self, v, visited):
        visited.add(v)

        for i in v.children:
            if i not in visited:
                self.dfs(i, visited)


    def countComponent(self):
        visited = set()
        numberOfComponent = 0
        for i in self.nodes:
            if i not in visited:
                numberOfComponent += 1
                self.dfs(i, visited)
        
        return numberOfComponent
        
node1 = GraphNode('1')
node2 = GraphNode('2')
node3 = GraphNode('3')
node4 = GraphNode('4')
node5 = GraphNode('5')
node6 = GraphNode('6')
node7 = GraphNode('7')


graph1 = Graph([node1, node2, node3, node4, node5, node6, node7])
graph1.add_edge(node1, node2)
graph1.add_edge(node1, node5)
graph1.add_edge(node2, node5)
graph1.add_edge(node3, node4)
graph1.add_edge(node4, node6)

print(graph1.countComponent())
