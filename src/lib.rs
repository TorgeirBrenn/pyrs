use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

// Module: matrix_operations
pub mod matrix_operations {
    // Function: multiply
    pub fn matrix_multiply(
        a: &Vec<Vec<i32>>,
        b: &Vec<Vec<i32>>,
    ) -> Option<Vec<Vec<i32>>> {
        // Check if columns of 'a' equals rows of 'b'
        if a[0].len() != b.len() {
            return None;
        }

        let num_rows_a = a.len();
        let num_cols_a = a[0].len();
        let num_cols_b = b[0].len();

        // Initialize a matrix of zeros
        let mut result = vec![vec![0; num_cols_b]; num_rows_a];

        // Perform matrix multiplication
        for i in 0..num_rows_a {
            for j in 0..num_cols_b {
                for k in 0..num_cols_a {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        Some(result)
    }
}

#[pymodule]
fn matrix_operations(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(matrix_multiply, m)?)?;
    Ok(())
}

#[pyfunction]
fn matrix_multiply(_py: Python, a: Vec<Vec<i32>>, b:Vec<Vec<i32>>) -> PyResult<Option<Vec<Vec<i32>>>> {
    Ok(matrix_operations::matrix_multiply(&a, &b))
}