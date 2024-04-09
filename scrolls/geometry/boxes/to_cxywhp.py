from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp, xyxyn_to_xyxyp
from scrolls.geometry.boxes.to_xywhp import xywh_to_xywhp, xywhn_to_xywhp
from scrolls.geometry.boxes.to_cxywh import xyxy_to_cxywh, xywh_to_cxywh
from scrolls.geometry.boxes.to_cxywhn import cxywh_to_cxywhn


def xyxy_to_cxywhp(bounding_boxes, image_size):
    xyxyp = xyxy_to_xyxyp(bounding_boxes, image_size)
    return xyxyp_to_cxywhp(xyxyp)


def xywh_to_cxywhp(bounding_boxes, image_size):
    xywhp = xywh_to_xywhp(bounding_boxes, image_size)
    return xywhp_to_cxywhp(xywhp)


def xyxyn_to_cxywhp(bounding_boxes):
    xyxyp = xyxyn_to_xyxyp(bounding_boxes)
    return xyxyp_to_cxywhp(xyxyp)


def xywhn_to_cxywhp(bounding_boxes):
    xywhp = xywhn_to_xywhp(bounding_boxes)
    return xywhp_to_cxywhp(xywhp)


def cxywh_to_cxywhp(bounding_boxes, image_size):
    return cxywh_to_cxywhn(bounding_boxes, image_size) * 100


def cxywhn_to_cxywhp(bounding_boxes):
    return bounding_boxes * 100


def xyxyp_to_cxywhp(bounding_boxes):
    return xyxy_to_cxywh(bounding_boxes)


def xywhp_to_cxywhp(bounding_boxes):
    return xywh_to_cxywh(bounding_boxes)


def cxywhp_to_cxywhp(bounding_boxes):
    return bounding_boxes
