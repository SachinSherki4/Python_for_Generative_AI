
import heapq

def dijkshtra(matrix, start):

    n = len(matrix)
    visited =[False] * n # keep track which node we have finished processing.
    distances = [float('inf')]* n  # we assuming all distance at start is infinite
    distances[start] = 0  # We set the distance to the starting node 0

    # use priority queue to always pick the nearest region/smallest distance next
    min_heap = [(0, start)] #(distance, node)
    #print(min_heap)
    while min_heap :
        current_dist, u = heapq.heappop(min_heap)
        #print(f"current_dist : {current_dist} and start : {u}")
        if visited[u]: # check if this node explore already or not
            continue # if yes, skipp
        visited[u]=True # add it to visited and mark it True

        for v in range(n) : # check all nebours of this region
            if matrix[u][v] > 0 and not visited[v]: # if neibour connected and distance more than zero and not explore
                new_dist = current_dist + matrix[u][v] # calculate new  distance
                if new_dist < distances[v]: # check new_dist less than already available distance then replace
                    distances[v] = new_dist
                    heapq.heappush(min_heap,(new_dist,v))
    return distances


