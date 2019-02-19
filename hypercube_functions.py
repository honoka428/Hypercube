def get_names(dimensions):
    """Returns a list of vertices for a hypercube of a given dimension."""
    if dimensions <= 0 or dimensions > 20:
        return []
    num_of_vertices = 2 ** dimensions
    names = []
    for i in range(num_of_vertices):
        old_bin = str(bin(i))
        new_bin = old_bin[2:]
        while len(new_bin) < dimensions:
            new_bin = '0' + new_bin
        names.append(new_bin)
    return names

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

def get_hypercube_neighbor_names(name, all_names):
    """Returns list of neighbor nodes for a given node."""
    neighbor_names = []
    for i in all_names:
        if i != name: #iterate through all other vertices except for with self
            if is_diff_by_one(name, i):
                neighbor_names.append("{}".format(i))
    return neighbor_names



#WRONG OUTPUT. Checks power of two difference

"""
def is_power_of_two(int_val):
    if int_val == 1:
        return True
    while int_val % 2 == 0:
        int_val = int_val // 2
        if int_val == 1:
            return True
    return False

def get_hypercube_neighbor_names_ver1(name, all_names): 
    neighbor_names = []
    for i in all_names:
        if i != name: #iterate through all other vertices except for with self
            difference = abs(int(i, 2) - int(name, 2))
            if is_power_of_two(difference):
                neighbor_names.append("{}".format(i))
    return "{} is connected to: {}".format(name, neighbor_names)
"""
