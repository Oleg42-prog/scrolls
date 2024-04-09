from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn
from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp


def xyxy_to_xywhp(bounding_boxes, image_size):
    xyxyp = xyxy_to_xyxyp(bounding_boxes, image_size)
    return xyxyp_to_xywhp(xyxyp)


def xywh_to_xywhp(bounding_boxes, image_size):
    return xywh_to_xywhn(bounding_boxes, image_size) * 100


def xyxyn_to_xywhp():
    pass


def xywhn_to_xywhp(bounding_boxes):
    return bounding_boxes * 100


def cxywh_to_xywhp():
    pass


def cxywhn_to_xywhp():
    pass


def xyxyp_to_xywhp(bounding_boxes):
    return xyxy_to_xywh(bounding_boxes)


def xywhp_to_xywhp(bounding_boxes):
    return bounding_boxes


def cxywhp_to_xywhp(bounding_boxes):
    return cxywh_to_xywh(bounding_boxes)
