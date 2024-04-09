from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp, xyxyn_to_xyxyp
from scrolls.geometry.boxes.to_xywhp import xywh_to_xywhp, xywhn_to_xywhp
from scrolls.geometry.boxes.to_cxywh import xyxy_to_cxywh, xywh_to_cxywh
from scrolls.geometry.boxes.to_cxywhn import cxywh_to_cxywhn


def xyxy_to_cxywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    return xyxyp_to_cxywhp(xyxyp)


def xywh_to_cxywhp(xywh, image_size):
    xywhp = xywh_to_xywhp(xywh, image_size)
    return xywhp_to_cxywhp(xywhp)


def xyxyn_to_cxywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    return xyxyp_to_cxywhp(xyxyp)


def xywhn_to_cxywhp(xywhn):
    xywhp = xywhn_to_xywhp(xywhn)
    return xywhp_to_cxywhp(xywhp)


def cxywh_to_cxywhp(cxywh, image_size):
    return cxywh_to_cxywhn(cxywh, image_size) * 100


def cxywhn_to_cxywhp(cxywhn):
    return cxywhn * 100


def xyxyp_to_cxywhp(xyxyp):
    return xyxy_to_cxywh(xyxyp)


def xywhp_to_cxywhp(xywhp):
    return xywh_to_cxywh(xywhp)


def cxywhp_to_cxywhp(cxywhp):
    return cxywhp
