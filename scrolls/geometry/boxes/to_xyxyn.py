from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy


def xyxy_to_xyxyn(xyxy, image_size):
    xyxyn = normalize_bounding_boxes(xyxy, image_size)
    return xyxyn


def xywh_to_xyxyn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def xyxyn_to_xyxyn(xyxyn):
    return xyxyn


def xywhn_to_xyxyn(xywhn):
    xyxyn = xywh_to_xyxy(xywhn)
    return xyxyn


def cxywh_to_xyxyn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywhn_to_xyxyn(cxywhn):
    return cxywh_to_xyxy(cxywhn)


def xyxyp_to_xyxyn(xyxyp):
    xyxyn = xyxyp / 100
    return xyxyn


def xywhp_to_xyxyn(xywhp):
    xywhn = xywhp / 100
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = cxywhp / 100
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn
