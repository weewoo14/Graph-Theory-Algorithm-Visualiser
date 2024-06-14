from settings import *
class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
minimum_spanning_tree = []
def kruskals_algorithm(graph, node_count,edge_count):
    disjoint_set = DisjointSet(node_count)
    mst = [[] for i in range(node_count+1)]
    paths = []
    temp_edges = [[1,2,3],
    [1,3,6],
    [2,4,5],
    [2,7,3],
    [3,6,1],
    [3,7,2],
    [4,5,10],
    [4,8,4]]
    edges = sorted(temp_edges,key=lambda x:x[2])
    for u,v,w in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u,v)
            paths.append([u,v,w])
    return paths

