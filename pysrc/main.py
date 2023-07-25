import timeit
from functools import partial

from utils import random_matrix, matrix_multiply as py_matrix_multiply
from matrix_operations import matrix_multiply as rs_matrix_multiply


def compare_performance(matrix_size: int, iterations: int):
    print("-" * 110)
    print(
        f"Comparing Rust and Python functions for matrix multiplication using matrix size "
        f"{matrix_size}x{matrix_size} over {iterations} iteration(s)."
    )

    py_time, rs_time = 0.0, 0.0
    for _ in range(iterations):
        a = random_matrix(matrix_size)
        b = random_matrix(matrix_size)

        py_time += timeit.timeit(partial(py_matrix_multiply, a, b), number=1)
        rs_time += timeit.timeit(partial(rs_matrix_multiply, a, b), number=1)

    # # Sample matrices to multiply
    # a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    #
    # # Wrap the function calls in another function so that they can be timed
    # def py_multiply():
    #     return py_matrix_multiply(a, b)
    #
    # def rs_multiply():
    #     return rs_matrix_multiply(a, b)
    #
    # # Time the functions
    # py_time = timeit.timeit(py_multiply, number=1000)
    # rs_time = timeit.timeit(rs_multiply, number=1000)

    # Print the results
    print(f"Python function took an average of {py_time / iterations:.2e} seconds.")
    print(f"Rust function took an average of {rs_time / iterations:.2e} seconds.")
    print(
        f"Rust function took {rs_time / py_time * 100:.2f} % the time of the python function."
    )
    print("-" * 110)


if __name__ == "__main__":
    compare_performance(3, 10000)
    compare_performance(10, 1000)
    compare_performance(100, 100)
    compare_performance(1000, 3)
