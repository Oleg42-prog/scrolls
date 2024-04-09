from scrolls.geometry.boxes.transforms import normalize_bounding_boxes, rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy as boxes_xywh_to_xyxy, cxywh_to_xyxy as boxes_cxywh_to_xyxy
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh as boxes_xyxy_to_xywh, cxywh_to_xywh as boxes_cxywh_to_xywh
from scrolls.geometry.boxes.to_cxywh import xywh_to_cxywh as boxes_xywh_to_cxywh, xyxy_to_cxywh as boxes_xyxy_to_cxywh


def box_xyxy_to_xywh(bounding_box):
    bounding_boxes = bounding_box.reshape(1, -1)
    return boxes_xyxy_to_xywh(bounding_boxes)


# From percentage

def boxes_xyxyp_to_xyxy(bounding_boxes, image_size):
    bounding_boxes_normalized = bounding_boxes / 100
    return rescale_bounding_boxes(bounding_boxes_normalized, image_size)


def boxes_xywhp_to_xywh(bounding_boxes, image_size):
    bounding_boxes_normalized = bounding_boxes / 100
    return rescale_bounding_boxes(bounding_boxes_normalized, image_size)


def boxes_cxywhp_to_cxywh(bounding_boxes, image_size):
    bounding_boxes_normalized = bounding_boxes / 100
    return rescale_bounding_boxes(bounding_boxes_normalized, image_size)
