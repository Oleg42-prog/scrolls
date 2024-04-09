from scrolls.geometry.boxes.to_cxywh import xyxy_to_cxywh, xywh_to_cxywh
from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn
from scrolls.geometry.boxes.to_xyxyn import xyxyp_to_xyxyn
from scrolls.geometry.boxes.to_xywhn import xywhp_to_xywhn


def xyxy_to_cxywhn(bounding_boxes, image_size):
    xyxyn = xyxy_to_xyxyn(bounding_boxes, image_size)
    return xyxyn_to_cxywhn(xyxyn)


def xywh_to_cxywhn(bounding_boxes, image_size):
    xywhn = xywh_to_xywhn(bounding_boxes, image_size)
    return xywhn_to_cxywhn(xywhn)


def xyxyn_to_cxywhn(bounding_boxes):
    return xyxy_to_cxywh(bounding_boxes)


def xywhn_to_cxywhn(bounding_boxes):
    return xywh_to_cxywh(bounding_boxes)


def cxywh_to_cxywhn(bounding_boxes, image_size):
    return normalize_bounding_boxes(bounding_boxes, image_size)


def cxywhn_to_cxywhn(bounding_boxes):
    return bounding_boxes


def xyxyp_to_cxywhn(bounding_boxes):
    xyxyn = xyxyp_to_xyxyn(bounding_boxes)
    return xyxyn_to_cxywhn(xyxyn)


def xywhp_to_cxywhn(bounding_boxes):
    xywhn = xywhp_to_xywhn(bounding_boxes)
    return xywhn_to_cxywhn(xywhn)


def cxywhp_to_cxywhn(bounding_boxes):
    return bounding_boxes / 100
