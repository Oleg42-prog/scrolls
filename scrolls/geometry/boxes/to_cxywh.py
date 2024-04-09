import numpy as np
from scrolls.geometry.linal import apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy, xyxyp_to_xyxy
from scrolls.geometry.boxes.to_xywh import xywhn_to_xywh, xywhp_to_xywh


def xyxy_to_cxywh(bounding_boxes):
    transformation_matrix = np.array([
        [0.5, 0, 0.5, 0],
        [0, 0.5, 0.5, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def xywh_to_cxywh(bounding_boxes):
    transformation_matrix = np.array([
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return apply_linear_operator(transformation_matrix, bounding_boxes)


def xyxyn_to_cxywh(bounding_boxes, image_size):
    xyxy = xyxyn_to_xyxy(bounding_boxes, image_size)
    return xyxy_to_cxywh(xyxy)


def xywhn_to_cxywh(bounding_boxes, image_size):
    xywh = xywhn_to_xywh(bounding_boxes, image_size)
    return xywh_to_cxywh(xywh)


def cxywh_to_cxywh(bounding_boxes):
    return bounding_boxes


def cxywhn_to_cxywh(bounding_boxes, image_size):
    return rescale_bounding_boxes(bounding_boxes, image_size)


def xyxyp_to_cxywh(bouding_boxes, image_size):
    xyxy = xyxyp_to_xyxy(bouding_boxes, image_size)
    return xyxy_to_cxywh(xyxy)


def xywhp_to_cxywh(bounding_boxes, image_size):
    xywh = xywhp_to_xywh(bounding_boxes, image_size)
    return xywh_to_cxywh(xywh)


def cxywhp_to_cxywh(bounding_boxes, image_size):
    bounding_boxes_normalized = bounding_boxes / 100
    return rescale_bounding_boxes(bounding_boxes_normalized, image_size)
