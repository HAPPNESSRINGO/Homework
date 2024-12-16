from lab9_ex3_transpose_matrix import transpose_matrix

def test_empty_matrix():
    assert transpose_matrix([]) == []

def test_single_element():
    assert transpose_matrix([[42]]) == [[42]]

def test_single_row():
    # Original is 1x3 matrix, transpose should be 3x1
    assert transpose_matrix([[1,2,3]]) == [[1],[2],[3]]

def test_single_column():
    # Original is 3x1 matrix, transpose should be 1x3
    assert transpose_matrix([[1],[2],[3]]) == [[1,2,3]]

def test_square_matrix():
    # Original 2x2
    assert transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]]

def test_rectangular_matrix():
    # Original 2x3: [[1,2,3],[4,5,6]]
    # Transpose should be 3x2: [[1,4],[2,5],[3,6]]
    assert transpose_matrix([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]