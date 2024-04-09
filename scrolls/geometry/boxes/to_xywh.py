import numpy as np
from scrolls.geometry.linal import apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy
from scrolls.geometry.boxes.to_cxywh import cxywhn_to_cxywh


def xyxy_to_xywh(bounding_boxes):
    transformation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def xywh_to_xywh(bounding_boxes):
    return bounding_boxes


def xyxyn_to_xywh(bounding_boxes, image_size):
    xyxy = xyxyn_to_xyxy(bounding_boxes, image_size)
    return xyxy_to_xywh(xyxy)


def xywhn_to_xywh(bounding_boxes, image_size):
    return rescale_bounding_boxes(bounding_boxes, image_size)


def cxywh_to_xywh(bounding_boxes):
    transformation_matrix = np.array([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def cxywhn_to_xywh(bounding_boxes, image_size):
    cxywh = cxywhn_to_cxywh(bounding_boxes, image_size)
    return cxywh_to_xywh(cxywh)


def xyxyp_to_xywh():
    pass


def xywhp_to_xywh(bounding_boxes, image_size):
    bounding_boxes_normalized = bounding_boxes / 100
    return rescale_bounding_boxes(bounding_boxes_normalized, image_size)


def cxywhp_to_xywh():
    pass
