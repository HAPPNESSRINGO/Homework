def read_matrix(filename: str) -> list[list[int]]:
	"""
    Read a matrix from a text file.
    Each line in the file represents a row in the matrix.
    Each row is a line of integers separated by space.

    :param filename: The name of the input file.
    :return: A list of lists of integers representing the matrix.
    """
	matrix = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if line:  # To handle empty lines, if any
				# Split the line by spaces and convert each part to int
				row = [int(x) for x in line.split()]
				matrix.append(row)
	return matrix


def transpose_matrix_from_file(input_filename: str) -> list[list[int]]:
	"""
    Read the matrix from input_filename, transpose it, and return the transposed matrix.

    Transposing a matrix means converting rows to columns and columns to rows:
    If original matrix has size N×M, the transposed matrix has size M×N.

    :param input_filename: The name of the file containing the matrix.
    :return: A list of lists of integers representing the transposed matrix.
    """
	# First read the matrix from the file
	original = read_matrix(input_filename)

	# If the matrix is empty, just return empty
	if not original:
		return []

	# Determine dimensions
	rows = len(original)
	cols = len(original[0])

	# Construct the transposed matrix
	transposed = []
	for j in range(cols):
		new_row = []
		for i in range(rows):
			new_row.append(original[i][j])
		transposed.append(new_row)

	return transposed
