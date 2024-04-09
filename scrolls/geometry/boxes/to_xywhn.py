from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xyxyp_to_xyxyn
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_cxywhn import cxywh_to_cxywhn, cxywhp_to_cxywhn


def xyxy_to_xywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def xywh_to_xywhn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    return xywhn


def xyxyn_to_xywhn(xyxyn):
    xywhn = xyxy_to_xywh(xyxyn)
    return xywhn


def xywhn_to_xywhn(xywhn):
    return xywhn


def cxywh_to_xywhn(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    xywhn = cxywhn_to_xywhn(cxywhn)
    return xywhn


def cxywhn_to_xywhn(cxywhn):
    xywhn = cxywh_to_xywh(cxywhn)
    return xywhn


def xyxyp_to_xywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def xywhp_to_xywhn(xywhp):
    xywhn = xywhp / 100
    return xywhn


def cxywhp_to_xywhn(cxywhp):
    cxywhp = cxywhp_to_cxywhn(cxywhp)
    xywhn = cxywhn_to_xywhn(cxywhp)
    return xywhn
