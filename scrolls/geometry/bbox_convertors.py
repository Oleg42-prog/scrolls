import numpy as np
from scrolls.geometry.linal import apply_linear_operator


def normalize_bounding_boxes(bounding_boxes, image_size):
    image_width, image_height = image_size
    transformation_vector = np.array([image_width, image_height, image_width, image_height])
    return bounding_boxes / transformation_vector


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
    return normalize_bounding_boxes(bounding_boxes, image_size)


def boxes_xywh_to_xywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def boxes_cxywh_to_cxywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def boxes_xyxy_to_xyxyp(bounding_boxes, image_size):
    return boxes_xyxy_to_xyxyn(bounding_boxes, image_size) * 100


def boxes_xywh_to_xywhp(bounding_boxes, image_size):
    return boxes_xywh_to_xywhn(bounding_boxes, image_size) * 100


def boxes_cxywh_to_cxywhp(bounding_boxes, image_size):
    return boxes_cxywh_to_cxywhn(bounding_boxes, image_size) * 100


def boxes_xyxyp_to_xyxyn(bounding_boxes):
    return bounding_boxes / 100


def boxes_xywhp_to_xywhn(bounding_boxes):
    return bounding_boxes / 100


def boxes_cxywhp_to_cxywhn(bounding_boxes):
    return bounding_boxes / 100
