import numpy as np


def matrix_map(func, matrix):
    return [list(map(func, row)) for row in matrix]


def np_matrix_stack(matrix):
    rows = list(map(np.hstack, matrix))
    return np.vstack(rows)


def flatten(matrix):
    return [elem for row in matrix for elem in row]
