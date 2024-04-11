from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp, xyxyn_to_xyxyp
from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn
from scrolls.geometry.boxes.to_cxywhp import cxywh_to_cxywhp


def xyxy_to_xywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xywh_to_xywhp(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    xywhp = xywhn * 100
    return xywhp


def xyxyn_to_xywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xywhn_to_xywhp(xywhn):
    xywhp = xywhn * 100
    return xywhp


def cxywh_to_xywhp(cxywh, image_size):
    cxywhp = cxywh_to_cxywhp(cxywh, image_size)
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp


def cxywhn_to_xywhp(cxywhn):
    cxywhp = cxywhn * 100
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp


def xyxyp_to_xywhp(xyxyp):
    xywhp = xyxy_to_xywh(xyxyp)
    return xywhp


from scrolls.geometry.boxes.convertors.identity import xywhp_to_xywhp


def cxywhp_to_xywhp(cxywhp):
    xywhp = cxywh_to_xywh(cxywhp)
    return xywhp
