import numpy as np


def min_max_scaller(array: np.ndarray) -> np.ndarray:
    min_value = array.min()
    max_value = array.max()
    return (array - min_value) / (max_value - min_value)
