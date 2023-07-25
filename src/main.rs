use matrix_operations::matrix_operations::matrix_multiply;

fn main() {
    let a = vec![vec![1, 2, 3], vec![4, 5, 6]];
    let b = vec![vec![7, 8], vec![9, 10], vec![11, 12]];
    let result = matrix_multiply(&a, &b);
    match result {
        Some(matrix) => println!("{:?}", matrix),
        None => println!("These matrices cannot be multiplied"),
    }
}