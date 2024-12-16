from lab9_ex4_transpose_matrix_from_file import read_matrix, transpose_matrix_from_file


def test_read_matrix_empty_file_returns_empty_list():
    """
    Test that read_matrix returns an empty list when the file is empty.
    """
    result = read_matrix("example_matrix_empty.txt")
    assert result == []

def test_read_matrix_single_line_returns_single_row():
    """
    Test that read_matrix returns a single-row matrix from a single-line file.
    """
    result = read_matrix("example_matrix_single_line.txt")
    assert result == [[1, 2, 3]]

def test_transpose_matrix_from_file_empty_file_returns_empty_list():
    """
    Test that transpose_matrix_from_file returns an empty list if the original file is empty.
    """
    result = transpose_matrix_from_file("example_matrix_empty.txt")
    assert result == []

def test_transpose_matrix_from_file_2x2_returns_correct_transpose():
    """
    Test that transpose_matrix_from_file returns the correct transpose for a 2x2 matrix.
    Original:
      1 2
      3 4
    Transpose:
      1 3
      2 4
    """
    result = transpose_matrix_from_file("example_matrix_2x2.txt")
    assert result == [[1, 3], [2, 4]]

def test_transpose_matrix_from_file_2x3_returns_correct_transpose():
    """
    Test that transpose_matrix_from_file returns the correct transpose for a 2x3 matrix.
    Original:
      1 2 3
      4 5 6
    Transpose:
      1 4
      2 5
      3 6
    """
    result = transpose_matrix_from_file("example_matrix_2x3.txt")
    assert result == [[1,4],[2,5],[3,6]]

def test_read_matrix_example_matrix():
    """
    Test that read_matrix correctly reads example_matrix.txt with the new content:
      1   2   3   5
      5  -6   1   9
     -5   6   9  -17
    """
    result = read_matrix("example_matrix.txt")
    expected = [
        [1,  2,  3,   5],
        [5, -6,  1,   9],
        [-5, 6,  9, -17]
    ]
    assert result == expected

def test_transpose_matrix_from_file_example_matrix():
    """
    Test that transpose_matrix_from_file returns the correct transpose for the updated example_matrix.txt.
    Given:
      1   2   3   5
      5  -6   1   9
     -5   6   9  -17

    The transpose (4x3) should be:
      1   5  -5
      2  -6   6
      3   1   9
      5   9  -17
    """
    result = transpose_matrix_from_file("example_matrix.txt")
    expected = [
        [1,   5,  -5],
        [2,  -6,   6],
        [3,   1,   9],
        [5,   9, -17]
    ]
    assert result == expected