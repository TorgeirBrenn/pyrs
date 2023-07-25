import pytest
from matrix_operations import matrix_multiply as matrix_multiply_rs
from utils import matrix_multiply

test_data = [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
        [[84, 90, 96], [201, 216, 231], [318, 342, 366]],
    ),
    ([[1, 2], [3, 4]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    ([[1, 2], [3, 4]], [[1, 0], [0, 1]], [[1, 2], [3, 4]]),
    ([[1, 2, 3]], [[4], [5], [6]], [[32]]),
]


@pytest.mark.parametrize("a, b, expected_result", test_data)
def test_matrix_multiply(a, b, expected_result):
    py_result = matrix_multiply(a, b)
    assert py_result == expected_result

    rs_result = matrix_multiply_rs(a, b)
    assert rs_result == expected_result
