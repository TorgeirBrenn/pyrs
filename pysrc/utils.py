import random

Matrix = list[list[int]]


def random_matrix(n: int, min_val: int = 0, max_val: int = 100) -> Matrix:
    """Generate a random square matrix of size n x n."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]


def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    """
    Compute the multiplication of two matrices: 'a' and 'b'.

    This function performs matrix multiplication where it multiplies matrix 'a' by matrix 'b'.
    The number of columns in 'a' and the number of rows in 'b' must align for multiplication to be possible.

    Args:
        a (Matrix): The first matrix of integers. It is a 2-D list where inner lists are rows of the matrix.
        b (Matrix): The second matrix of integers. It is a 2-D list where inner lists are rows of the matrix.

    Returns:
        Matrix: The multiplication result of matrix 'a' and 'b'. It is a 2-D list where inner lists are rows of the resulting matrix.

    Raises:
        ValueError: If 'a' and 'b' are not matrices, or if the number of columns in 'a' does not equal the number of rows in 'b.

    Examples:
        >>> a = [[1, 2, 3], [4, 5, 6]]
        >>> b = [[7, 8], [9, 10], [11, 12]]
        >>> matrix_multiply(a, b)
        [[58, 64], [139, 154]]
    """
    num_rows_a = len(a)
    num_cols_a = len(a[0])
    num_cols_b = len(b[0])

    # Instantiate matrix of zeros
    result = [[0 for row in range(num_cols_b)] for col in range(num_rows_a)]

    # Perform matrix multiplication
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            for k in range(num_cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result
