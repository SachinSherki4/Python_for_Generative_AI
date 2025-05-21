
import heapq

class CityRoadNetwork:
    def __init__(self, regions):
        self.regions=regions
        self.size= len(regions)
        self.region_index= {name : i for i, name in enumerate(self.regions)}
        self.matrix = [[0] * self.size for _ in range(self.size)]
        self.blocked_edge= set() # edges are tuple (i,j)
        self.blocked_node = set() # destination

    def add_road(self,from_region, to_region, distance):
        i= self.region_index[from_region]
        j= self.region_index[to_region]
        self.matrix[i][j] = distance
        self.matrix[j][i] = distance

    # add blocked road into blocked road/edge tuple
    def blocked_road(self, from_region, to_region):
        i = self.region_index[from_region]
        j = self.region_index[to_region]
        self.blocked_edge.add((i,j))
        self.blocked_edge.add((j,i))

    # not add available road in blocked node = discard
    def unblocked_road(self,from_region, to_region):
        i = self.region_index[from_region]
        j = self.region_index[to_region]
        self.blocked_edge.discard((i, j))
        self.blocked_edge.discard((j, i))

    # identify blocked area
    def blocked_region(self,region):
        self.blocked_node.add(self.region_index[region])


    def unblocked_region(self,region):
        self.blocked_node.discard(self.region_index[region])

    # check if area/region is accessible or not
    def is_accesible(self, i,j):
        return (i not in self.blocked_node and j not in self.blocked_node and
                (i,j) not in self.blocked_edge and self.matrix[i][j] > 0)

    def print_matrix(self):
        print("     "+ "  ".join(self.regions))
        for i, row in enumerate(self.matrix):
            row_dist=" ".join(f"{dist:2}" if dist > 0 else " ." for dist in row)
            print(f"{self.regions[i]} : {row_dist}")