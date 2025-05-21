
class RoadMap :
    def __init__(self, regions):
        """
        Initialize a graph for the smart city.
        :param regions: List of region names (e.g., ['A', 'B', 'C', 'D', 'E'])
        """
        self.regions = regions
        self.size= len(regions)
        # here we are creating dictionary where if found same key, it add value as array
        self.region_index = {region : i for i, region in enumerate(regions)} # a
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def add_road(self, from_region, to_region, distance):
        """
        Adds a two-way (undirected) road between regions.
        :param from_region: Name of the source region
        :param to_region: Name of the destination region
        :param distance: Distance or weight
        """
        i=self.region_index[from_region]
        j= self.region_index[to_region]

        self.matrix[i][j] = distance
        self.matrix[j][i] = distance # unidirected

    def display_map(self):
        print("🗺️ Road Map (Adjacency Matrix):")
        print(" "+" ".join(self.regions))
        for i in range(self.size):
            print(f" {self.regions[i]} " + " ".join({self.matrix[i][j]}) for j in range(self.size))




