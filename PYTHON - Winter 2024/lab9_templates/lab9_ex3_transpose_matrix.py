def transpose_matrix(a_matrix: list[list[int]]) -> list[list[int]]:
	"""
    Given a matrix a_matrix of size N×M (N rows, M columns),
    return its transpose, which is a matrix of size M×N.

    Transpose definition:
    For each valid i,j:
    A'[i][j] = A[j][i]

    :param a_matrix: A list of lists of integers representing the original matrix.
    :return: A new list of lists of integers representing the transposed matrix.
    """
	# If the matrix is empty, return empty
	if not a_matrix:
		return []

	# Get the dimensions of the original matrix
	rows = len(a_matrix)
	cols = len(a_matrix[0])

	# Construct the transposed matrix
	# Transposed has 'cols' rows and 'rows' columns
	transposed = []
	for j in range(cols):
		new_row = []
		for i in range(rows):
			new_row.append(a_matrix[i][j])
		transposed.append(new_row)

	return transposed
