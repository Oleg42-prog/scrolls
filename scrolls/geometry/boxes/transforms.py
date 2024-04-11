import numpy as np


def normalize_bounding_boxes(bounding_boxes, original_size):
    original_width, original_height = original_size
    transformation_vector = np.array([original_width, original_height, original_width, original_height])
    return bounding_boxes / transformation_vector


def rescale_bounding_boxes(bounding_boxes, original_size):
    original_width, original_height = original_size
    transformation_vector = np.array([original_width, original_height, original_width, original_height])
    return bounding_boxes * transformation_vector
