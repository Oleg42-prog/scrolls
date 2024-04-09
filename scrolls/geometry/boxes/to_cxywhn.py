from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xyxyp_to_xyxyn
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn, xywhp_to_xywhn
from scrolls.geometry.boxes.to_cxywh import xyxy_to_cxywh, xywh_to_cxywh


def xyxy_to_cxywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    return xyxyn_to_cxywhn(xyxyn)


def xywh_to_cxywhn(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    return xywhn_to_cxywhn(xywhn)


def xyxyn_to_cxywhn(xyxyn):
    return xyxy_to_cxywh(xyxyn)


def xywhn_to_cxywhn(xywhn):
    return xywh_to_cxywh(xywhn)


def cxywh_to_cxywhn(cxywh, image_size):
    return normalize_bounding_boxes(cxywh, image_size)


def cxywhn_to_cxywhn(cxywhn):
    return cxywhn


def xyxyp_to_cxywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    return xyxyn_to_cxywhn(xyxyn)


def xywhp_to_cxywhn(xywhp):
    xywhn = xywhp_to_xywhn(xywhp)
    return xywhn_to_cxywhn(xywhn)


def cxywhp_to_cxywhn(cxywhp):
    return cxywhp / 100
