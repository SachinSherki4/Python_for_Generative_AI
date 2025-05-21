
from cityRoadNetwork import CityRoadNetwork
from dijkshtra_algorithm import dijkshtra_algo


regions= ['A', 'B', 'C', 'D', 'E', 'F']
cityNetwork= CityRoadNetwork(regions)
cityNetwork.print_matrix()

cityNetwork.add_road('A', 'B', 3)
cityNetwork.add_road('A', 'C', 2)
cityNetwork.add_road('B', 'D', 4)
cityNetwork.add_road('C', 'D', 1)
cityNetwork.add_road('C', 'E', 7)
cityNetwork.add_road('D', 'F', 3)
cityNetwork.add_road('E', 'F', 1)

cityNetwork.print_matrix()

cityNetwork.blocked_road('C','D')
cityNetwork.blocked_region('E')

distances = dijkshtra_algo(cityNetwork, 'A')

print("Shortest distances from region A:")
for region, dist in zip(regions, distances):
    status = "Blocked" if cityNetwork.region_index[region] in cityNetwork.blocked_node else dist
    print(f"A -> {region} : {status}")

"""
Shortest distances from region A:
A -> A : 0
A -> B : 3
A -> C : 2
A -> D : 7
A -> E : Blocked
A -> F : 10
"""