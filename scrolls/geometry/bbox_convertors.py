import numpy as np
from scrolls.geometry.linal import apply_linear_operator


def box_xyxy_to_xywh(bounding_box):
    bounding_boxes = bounding_box.reshape(1, -1)
    return boxes_xyxy_to_xywh(bounding_boxes)


def boxes_xyxy_to_xywh(bounding_boxes):
    transformation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def boxes_xywh_to_xyxy(bounding_boxes):
    transformation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def boxes_xyxy_to_xyxyn(bounding_boxes, image_size):
    image_width, image_height = image_size
    transformation_vector = np.array([image_width, image_height, image_width, image_height])
    return bounding_boxes / transformation_vector
