
from Python_DSA.Graphs.project1_smart_city_road.graph_matrix import RoadMap
from Python_DSA.Graphs.project1_smart_city_road.dijkshtra import dijkshtra

regions = ['A', 'B', 'C', 'D', 'E']
roadmap = RoadMap(regions)

#print(roadmap.matrix)
# Step 2: Connect roads (undirected edges with distances)
roadmap.add_road('A', 'B', 4)
roadmap.add_road('A', 'C', 2)
roadmap.add_road('B', 'C', 5)
roadmap.add_road('B', 'D', 10)
roadmap.add_road('C', 'D', 3)
roadmap.add_road('D', 'E', 1)

#roadmap.display_map()

start_index= regions.index('A')
distances = dijkshtra(roadmap.matrix, start_index)
for i, dist in enumerate(distances):
    print(f"A  to {regions[i]} : {dist} KM")

