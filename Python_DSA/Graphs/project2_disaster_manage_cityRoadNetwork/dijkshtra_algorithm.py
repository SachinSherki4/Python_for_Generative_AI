
import heapq

def dijkshtra_algo(network, start):

    n = network.size
    visited = [False] * n
    distances = [float('inf')] * n
    start_index = network.region_index[start]
    distances[start_index] = 0
    heap = [(0, start_index)]

    while heap :
        current_dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u]=True

        for v in range(n):
            if network.is_accesible(u,v) and not visited[v]:
                new_distance = current_dist + network.matrix[u][v]
                if new_distance < distances[v]:
                    distances[v]= new_distance
                    heapq.heappush(heap, (new_distance,v))
    return distances

