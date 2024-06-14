from settings import *
from heapq import heappush,heappop

def dijkstras_algorithm(graph,node_count,starting_node):
    paths = []
    pq_description = []
    distances = [float('inf') for i in range(node_count+1)]
    distances[starting_node] = 0
    priority_queue = [(0,starting_node)]
    while priority_queue:
        current_weight,current_node = heappop(priority_queue)
        if current_weight > distances[current_node]:
            continue
        for next_node,weight in graph[current_node]:
            new_distance = current_weight + weight
            if new_distance < distances[next_node]:
                paths.append([current_node,next_node])
                distances[next_node] = new_distance
                heappush(priority_queue,(new_distance,next_node))
        pq_description.append(list(priority_queue))
    return paths,pq_description