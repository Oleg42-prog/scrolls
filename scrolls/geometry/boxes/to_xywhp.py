from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp, xyxyn_to_xyxyp
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn
from scrolls.geometry.boxes.to_cxywhp import cxywh_to_cxywhp


def xyxy_to_xywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    return xyxyp_to_xywhp(xyxyp)


def xywh_to_xywhp(xywh, image_size):
    return xywh_to_xywhn(xywh, image_size) * 100


def xyxyn_to_xywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    return xyxyp_to_xywhp(xyxyp)


def xywhn_to_xywhp(xywhn):
    return xywhn * 100


def cxywh_to_xywhp(cxywh, image_size):
    cxywhp = cxywh_to_cxywhp(cxywh, image_size)
    return cxywhp_to_xywhp(cxywhp)


def cxywhn_to_xywhp(cxywhn):
    cxywhp = cxywhn * 100
    return cxywhp_to_xywhp(cxywhp)


def xyxyp_to_xywhp(xyxyp):
    return xyxy_to_xywh(xyxyp)


def xywhp_to_xywhp(xywhp):
    return xywhp


def cxywhp_to_xywhp(cxywhp):
    return cxywh_to_xywh(cxywhp)
