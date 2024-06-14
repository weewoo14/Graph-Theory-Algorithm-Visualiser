from settings import *

def depth_first_search(graph,node_count,starting_node):
    global paths
    paths = []
    visited = [False] * (node_count+1)
    visited[starting_node] = True
    def depth_search(graph,current_node,visit_array):
        global paths
        for next_node,weight in graph[current_node]:
            if not visit_array[next_node]:
                visit_array[next_node] = True
                paths.append([current_node,next_node])
                depth_search(graph,next_node,visit_array)
    depth_search(graph,starting_node,visited)
    return paths

