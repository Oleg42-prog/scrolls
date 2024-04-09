from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy
from scrolls.geometry.boxes.transforms import normalize_bounding_boxes


def xyxy_to_xyxyn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def xywh_to_xyxyn(bounding_boxes, image_size):
    bounding_boxes_normalized = normalize_bounding_boxes(bounding_boxes, image_size)
    return xywhn_to_xyxyn(bounding_boxes_normalized)


def xyxyn_to_xyxyn(bounding_boxes):
    return bounding_boxes


def xywhn_to_xyxyn(bounding_boxes):
    return xywh_to_xyxy(bounding_boxes)


def cxywh_to_xyxyn():
    pass


def cxywhn_to_xyxyn(bounding_boxes):
    return cxywh_to_xyxy(bounding_boxes)


def xyxyp_to_xyxyn(bounding_boxes):
    return bounding_boxes / 100


def xywhp_to_xyxyn():
    pass


def cxywhp_to_xyxyn():
    pass
