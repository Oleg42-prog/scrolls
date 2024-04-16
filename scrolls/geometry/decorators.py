import numpy as np


def empty_array_return(func):
    """
    Decorator that returns the input array if it is empty.
    The purpose of this decorator is to provide a convenient way to handle cases
    where an empty array is expected as an input to a function.
    """
    def inner(array, *args, **kwargs):

        if isinstance(array, np.ndarray):
            if array.size == 0:
                return array

        if isinstance(array, list):
            if array == []:
                return array

        if isinstance(array, tuple):
            if array == ():
                return array

        return func(array, *args, **kwargs)

    return inner
