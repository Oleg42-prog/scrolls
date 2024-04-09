from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy


def xyxy_to_xyxyn(xyxy, image_size):
    return normalize_bounding_boxes(xyxy, image_size)


def xywh_to_xyxyn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    return xywhn_to_xyxyn(xywhn)


def xyxyn_to_xyxyn(xyxyn):
    return xyxyn


def xywhn_to_xyxyn(xywhn):
    return xywh_to_xyxy(xywhn)


def cxywh_to_xyxyn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    return cxywhn_to_xyxyn(cxywhn)


def cxywhn_to_xyxyn(cxywhn):
    return cxywh_to_xyxy(cxywhn)


def xyxyp_to_xyxyn(xyxyp):
    return xyxyp / 100


def xywhp_to_xyxyn(xywhp):
    xywhn = xywhp / 100
    return xywhn_to_xyxyn(xywhn)


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = cxywhp / 100
    return cxywhn_to_xyxyn(cxywhn)
