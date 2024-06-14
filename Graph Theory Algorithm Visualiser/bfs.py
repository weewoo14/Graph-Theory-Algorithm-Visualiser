from collections import deque
from settings import *
def breadth_first_search(graph, node_count, starting_node):
    paths = []
    queue_description = []
    visited_array = [False] * (node_count + 1)
    queue = deque()
    queue.append(starting_node)
    visited_array[starting_node] = True
    while queue:
        current_node = queue.popleft()
        for next_node,weight in graph[current_node]:
            if not visited_array[next_node]:
                visited_array[next_node] = True
                queue.append(next_node)
                paths.append([current_node,next_node,weight])
        queue_description.append(list(queue))
    return paths,queue_description
