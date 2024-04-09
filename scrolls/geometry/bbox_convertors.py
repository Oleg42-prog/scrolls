from scrolls.geometry.boxes.transforms import normalize_bounding_boxes, rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy as boxes_xywh_to_xyxy, cxywh_to_xyxy as boxes_cxywh_to_xyxy
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh as boxes_xyxy_to_xywh, cxywh_to_xywh as boxes_cxywh_to_xywh
from scrolls.geometry.boxes.to_cxywh import xywh_to_cxywh as boxes_xywh_to_cxywh, xyxy_to_cxywh as boxes_xyxy_to_cxywh


def box_xyxy_to_xywh(bounding_box):
    bounding_boxes = bounding_box.reshape(1, -1)
    return boxes_xyxy_to_xywh(bounding_boxes)


# Converts of bounding box representations normalised synonyms
def boxes_xyxyn_to_xywhn(bounding_boxes):
    return boxes_xyxy_to_xywh(bounding_boxes)


def boxes_xywhn_to_xyxyn(bounding_boxes):
    return boxes_xywh_to_xyxy(bounding_boxes)


def boxes_xywhn_to_cxywhn(bounding_boxes):
    return boxes_xywh_to_cxywh(bounding_boxes)


def boxes_cxywhn_to_xywhn(bounding_boxes):
    return boxes_cxywh_to_xywh(bounding_boxes)


def boxes_cxywhn_to_xyxyn(bounding_boxes):
    return boxes_cxywh_to_xyxy(bounding_boxes)


def boxes_xyxyn_to_cxywhn(bounding_boxes):
    return boxes_xyxy_to_cxywh(bounding_boxes)


# Converts of bounding box representations percentage synonyms
def boxes_xyxyp_to_xywhp(bounding_boxes):
    return boxes_xyxy_to_xywh(bounding_boxes)


def boxes_xywhp_to_xyxyp(bounding_boxes):
    return boxes_xywh_to_xyxy(bounding_boxes)


def boxes_xywhp_to_cxywhp(bounding_boxes):
    return boxes_xywh_to_cxywh(bounding_boxes)


def boxes_cxywhp_to_xywhp(bounding_boxes):
    return boxes_cxywh_to_xywh(bounding_boxes)


def boxes_cxywhp_to_xyxyp(bounding_boxes):
    return boxes_cxywh_to_xyxy(bounding_boxes)


def boxes_xyxyp_to_cxywhp(bounding_boxes):
    return boxes_xyxy_to_cxywh(bounding_boxes)


# To normalized

def boxes_xyxy_to_xyxyn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def boxes_xywh_to_xywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def boxes_cxywh_to_cxywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


# From normalized

def boxes_xyxyn_to_xyxy(bounding_boxes, image_size):
    return rescale_bounding_boxes(bounding_boxes, image_size)


def boxes_xywhn_to_xywh(bounding_boxes, image_size):
    return rescale_bounding_boxes(bounding_boxes, image_size)


def boxes_cxywhn_to_cxywh(bounding_boxes, image_size):
    return rescale_bounding_boxes(bounding_boxes, image_size)


# To percentage

def boxes_xyxy_to_xyxyp(bounding_boxes, image_size):
    return boxes_xyxy_to_xyxyn(bounding_boxes, image_size) * 100


def boxes_xywh_to_xywhp(bounding_boxes, image_size):
    return boxes_xywh_to_xywhn(bounding_boxes, image_size) * 100


def boxes_cxywh_to_cxywhp(bounding_boxes, image_size):
    return boxes_cxywh_to_cxywhn(bounding_boxes, image_size) * 100


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
