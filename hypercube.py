def get_keys(dimensions):
    """Returns a list of all names(key) needed to construct hypercube of the given dimension."""
    if dimensions <= 0 or dimensions > 20:
        return []
    num_vertices = 2 ** dimensions
    all_keys = []
    for i in range(num_vertices):
        old_bin = str(bin(i))
        new_bin = old_bin[2:]
        while len(new_bin) < dimensions:
            new_bin = '0' + new_bin
        all_keys.append(new_bin)
    return all_keys

class Vertex:
    """Create Vertex object."""
    def __init__(self, key):
        """Key is a string."""
        self.id = key
        self.neighbors = []

    def __repr__(self):
        return "{}, {}".format(self.id, self.neighbors)

    def __str__(self): #Easy to read, for human consumption. __repr__  for niternal use. unambiguous and makesit easier to debug for developer
        """Returns id as a str value rather than location in memory."""
        return "{},{}".format(self.id, self.neighbors)

    @staticmethod
    def is_diff_by_one(name, i):
        """Returns whether two vertices differ by one bit value."""
        pos = 0
        count = 0
        while pos <= len(name) - 1:
            if name[pos] != i[pos]:
                count += 1
                pos += 1
            else:
                pos += 1
        if count == 1:
            return True
        return False

    def add_neighbors(self, key, all_keys):
        """Adds all neighbors of a given vertex to self.neighbors."""
        for i in all_keys:
            if i != key:
                if Vertex.is_diff_by_one(key, i):
                    self.neighbors.append("{}".format(i))
        return self.neighbors

    def get_id(self):
        """Returns id of a given vertex."""
        return self.id

    def get_neighbors(self):
        """Returns all neighbors of a given vertex."""
        return self.neighbors

class Hypercube:
    def __init__(self):
        self.num_vertices = 0
        self.vertices = []
        self.allverticesandneighbors = {} #dictionary: ordered, indexed, changeable, key:value

    def __repr__(self):
        return "{}".format(self.allverticesandneighbors)

    def __str__(self):
        return "{}".format(self.allverticesandneighbors)

    def add_vertices(self, all_keys):
        """Add vertex key as dict key: and its 'id' and 'neighbors' as value"""
        for key in all_keys:
            self.vertices.append(key)

    def get_vertices(self):
        return self.vertices

    def get_num_of_vert(self):
        self.num_vertices += len(self.vertices)
        return self.num_vertices

    def add_edges(self, key, vertices=None):
        vertices = self.vertices if vertices is None else vertices
        name = 0
        for i in key:
            new_vertex = Vertex(i)
            self.allverticesandneighbors[name] = new_vertex
            name += 1
            
    def get_all_connections(self):
        return self.allverticesandneighbors

hypercube_1 = Hypercube()
hypercube_1.add_edges(get_keys(1))
print(hypercube_1.get_all_connections())
