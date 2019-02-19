import hypercube_functions

def test_get_names_response_length():
    """Ensure function pre-conditions are working properly.
    Check that function returns correct number of vertices."""
    assert hypercube_functions.get_names(-100) == []
    assert hypercube_functions.get_names(0) == []
    assert hypercube_functions.get_names(100) == []
    assert len(hypercube_functions.get_names(1)) == 2
    assert len(hypercube_functions.get_names(2)) == 4
    assert len(hypercube_functions.get_names(4)) == 16
    assert len(hypercube_functions.get_names(6)) == 64
    assert len(hypercube_functions.get_names(10)) == 1024

def test_get_names_length_of_vals():
    """Ensure  all vertices returned are the correct length"""
    assert len(hypercube_functions.get_names(1)[0]) == 1
    assert len(hypercube_functions.get_names(5)[3]) == 5
    assert len(hypercube_functions.get_names(6)[2]) == 6
    assert len(hypercube_functions.get_names(10)[3]) == 10

def test_get_names_correct_vals():
    """Ensure function returns list with the correct values."""
    assert '0' in hypercube_functions.get_names(1)
    assert '11111' in hypercube_functions.get_names(5)
    assert '0000010101' in hypercube_functions.get_names(10)

def test_hypercube_neighbor_names():
    all_names = hypercube_functions.get_names(1)
    output = []
    for vertex in all_names:
        output.append(hypercube_functions.get_hypercube_neighbor_names(vertex, all_names))
    assert output == [['0'], ['1']] or [['1'], ['0']]

    all_names = hypercube_functions.get_names(3)
    output = []
    for vertex in all_names:
        output.append(hypercube_functions.get_hypercube_neighbor_names(vertex, all_names))
    assert output == [['001', '010', '100'], ['000', '011', '101'], ['000', '011', '110'],
                      ['001', '010', '111'], ['000', '101', '110'], ['001', '100', '111'],
                      ['010', '100', '111'], ['011', '101', '110']]
