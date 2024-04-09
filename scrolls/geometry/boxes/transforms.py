import numpy as np


def normalize_bounding_boxes(bounding_boxes, image_size):
    image_width, image_height = image_size
    transformation_vector = np.array([image_width, image_height, image_width, image_height])
    return bounding_boxes / transformation_vector


def rescale_bounding_boxes(bounding_boxes, image_size):
    image_width, image_height = image_size
    transformation_vector = np.array([image_width, image_height, image_width, image_height])
    return bounding_boxes * transformation_vector
