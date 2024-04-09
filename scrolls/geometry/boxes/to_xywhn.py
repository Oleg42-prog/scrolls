from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xyxyp_to_xyxyn
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_cxywhn import cxywh_to_cxywhn, cxywhp_to_cxywhn


def xyxy_to_xywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    return xyxyn_to_xywhn(xyxyn)


def xywh_to_xywhn(xywh, image_size):
    return normalize_bounding_boxes(xywh, image_size)


def xyxyn_to_xywhn(xyxyn):
    return xyxy_to_xywh(xyxyn)


def xywhn_to_xywhn(xywhn):
    return xywhn


def cxywh_to_xywhn(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    return cxywhn_to_xywhn(cxywhn)


def cxywhn_to_xywhn(cxywhn):
    return cxywh_to_xywh(cxywhn)


def xyxyp_to_xywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    return xyxyn_to_xywhn(xyxyn)


def xywhp_to_xywhn(xywhp):
    return xywhp / 100


def cxywhp_to_xywhn(cxywhp):
    cxywhp = cxywhp_to_cxywhn(cxywhp)
    return cxywhn_to_xywhn(cxywhp)
