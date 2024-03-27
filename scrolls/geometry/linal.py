import numpy as np


def min_max_scaller(array: np.ndarray) -> np.ndarray:
    min_value = array.min()
    max_value = array.max()
    return (array - min_value) / (max_value - min_value)


def apply_linear_operator(linear_operator, vectors):
    """
    Applies a linear operator to each vector in a set of vectors.

    This function is based on the following theorem:
    If A is a linear operator (represented as a square matrix), and X is a set of vectors {x1, x2, ..., xn}
    (represented as a matrix where rows are vectors x1, x2, ..., xn), then the result of applying the operator A
    to each vector from X can be calculated as Y = X @ A.T, where A.T is the transposed matrix A, @ is the
    matrix multiplication operator and Y := {A @ x1, A @ x2, ..., A @ xn} by definition.

    Parameters:
    linear_operator (np.ndarray): The linear operator, represented as a square matrix.
    vectors (np.ndarray): The set of vectors to which the operator will be applied, represented as a matrix where
    each row is a vector.

    Returns:
    np.ndarray: The result of applying the linear operator to each vector, represented as a matrix.
    """
    return vectors @ linear_operator.T
