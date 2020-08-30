
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


nodes = ["A", "B", "C", "D", "E"]
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "E"), ("D", "E")]

graph = Graph(nodes)
graph.print_graph()
print()

for u,v in edges:
    graph.add_edge(u, v)

graph.print_graph()


    