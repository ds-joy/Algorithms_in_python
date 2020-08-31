
class Graph:

    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []
    
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
    
    def print_graph(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])


nodes = []
no_of_nodes = int(input("Enter the number of nodes: "))

print("Enter the nodes:")
for i in range(no_of_nodes):
    nodes.append(input())



graph = Graph(nodes)
graph.print_graph()

n = int(input("Enter the number of edges: "))

print("Enter edges:")
for i in range(n):
    u, v = input().split()
    graph.add_edge(u, v)

graph.print_graph()


    