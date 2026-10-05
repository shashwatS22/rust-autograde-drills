use std::ops::{Add, Index, Mul};

use thiserror::Error;

#[derive(Debug, Error, PartialEq, Eq)]
pub enum MatrixError {
    #[error("dimension mismatch")]
    DimensionMismatch,
    #[error("index out of bounds")]
    OutOfBounds,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Matrix<T> {
    rows: usize,
    cols: usize,
    data: Vec<T>,
}

impl<T> Matrix<T> {
    pub fn new(rows: usize, cols: usize, data: Vec<T>) -> Result<Self, MatrixError> {
        todo!()
    }

    pub fn from_rows(rows: Vec<Vec<T>>) -> Result<Self, MatrixError> {
        todo!()
    }

    pub fn rows(&self) -> usize {
        todo!()
    }

    pub fn cols(&self) -> usize {
        todo!()
    }

    pub fn iter_rows(&self) -> MatrixRows<'_, T> {
        todo!()
    }
}

pub struct MatrixRows<'a, T> {
    matrix: &'a Matrix<T>,
    row: usize,
}

impl<'a, T> Iterator for MatrixRows<'a, T> {
    type Item = &'a [T];

    fn next(&mut self) -> Option<Self::Item> {
        todo!()
    }
}

impl<T> Index<(usize, usize)> for Matrix<T> {
    type Output = T;

    fn index(&self, (r, c): (usize, usize)) -> &Self::Output {
        todo!()
    }
}

impl<T> Add for Matrix<T>
where
    T: Copy + Add<Output = T>,
{
    type Output = Result<Matrix<T>, MatrixError>;

    fn add(self, rhs: Self) -> Self::Output {
        todo!()
    }
}

impl<T> Mul for Matrix<T>
where
    T: Copy + Add<Output = T> + Mul<Output = T> + Default,
{
    type Output = Result<Matrix<T>, MatrixError>;

    fn mul(self, rhs: Self) -> Self::Output {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore]
    fn new_valid_dimensions() {
        let m = Matrix::new(2, 2, vec![1, 2, 3, 4]).unwrap();
        assert_eq!(m.rows(), 2);
        assert_eq!(m.cols(), 2);
    }

    #[test]
    #[ignore]
    fn new_rejects_wrong_length() {
        assert_eq!(
            Matrix::<i32>::new(2, 2, vec![1, 2, 3]),
            Err(MatrixError::DimensionMismatch)
        );
    }

    #[test]
    #[ignore]
    fn index_and_add() {
        let a = Matrix::from_rows(vec![vec![1, 2], vec![3, 4]]).unwrap();
        let b = Matrix::from_rows(vec![vec![5, 6], vec![7, 8]]).unwrap();
        assert_eq!(a[(0, 1)], 2);
        let c = (a + b).unwrap();
        assert_eq!(c[(1, 1)], 12);
    }

    #[test]
    #[ignore]
    fn multiply_2x2() {
        let a = Matrix::from_rows(vec![vec![1, 2], vec![3, 4]]).unwrap();
        let b = Matrix::from_rows(vec![vec![2, 0], vec![1, 2]]).unwrap();
        let c = (a * b).unwrap();
        assert_eq!(c[(0, 0)], 4);
        assert_eq!(c[(1, 1)], 8);
    }

    #[test]
    #[ignore]
    fn iter_rows_yields_slices() {
        let m = Matrix::from_rows(vec![vec![1, 2], vec![3, 4]]).unwrap();
        let rows: Vec<_> = m.iter_rows().collect();
        assert_eq!(rows.len(), 2);
        assert_eq!(rows[0], &[1, 2]);
    }
}
