from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn
from scrolls.geometry.boxes.transforms import normalize_bounding_boxes


def xyxy_to_xywhn(bounding_boxes, image_size):
    xyxyn = xyxy_to_xyxyn(bounding_boxes, image_size)
    return xyxyn_to_xywhn(xyxyn)


def xywh_to_xywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def xyxyn_to_xywhn(bounding_boxes):
    return xyxy_to_xywh(bounding_boxes)


def xywhn_to_xywhn(bounding_boxes):
    return bounding_boxes


def cxywh_to_xywhn():
    pass


def cxywhn_to_xywhn(bounding_boxes):
    return cxywh_to_xywh(bounding_boxes)


def xyxyp_to_xywhn():
    pass


def xywhp_to_xywhn(bounding_boxes):
    return bounding_boxes / 100


def cxywhp_to_xywhn():
    pass
