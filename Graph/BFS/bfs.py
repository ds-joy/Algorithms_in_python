from queue import Queue

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

# bfs algo starts from here
def bfs(graph01):

    while not bfs_queue.empty():
        u = bfs_queue.get() # dequeue
        bfs_sequence.append(u)

        for v in graph01.adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1 
                bfs_queue.put(v)




# initializing and taking the graph
# as an input
nodes = []
no_of_nodes = int(input("Enter the number of nodes: "))
print("Enter the nodes:")
for i in range(no_of_nodes):
    nodes.append(input())

graph = Graph(nodes)

n = int(input("Enter the number of edges: "))
print("Enter edges:")
for i in range(n):
    u, v = input().split()
    graph.add_edge(u, v)

graph.print_graph()



visited = {}
level = {} # distance from the source
parent = {}
bfs_sequence = []

bfs_queue = Queue()

for node in graph.adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1 #inf

source = nodes[0]
visited[source] = True
level[source] = 0

bfs_queue.put(source) #enqueue

bfs(graph)

print("\n" + "The graph was traversed in this sequence:")
print(bfs_sequence)



    