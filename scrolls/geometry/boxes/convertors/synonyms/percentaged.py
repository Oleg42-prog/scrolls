from scrolls.geometry.boxes.convertors.representation import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy, cxywh_to_xywh


def xyxyp_to_xywhp(xyxyp):
    xywhp = xyxy_to_xywh(xyxyp)
    return xywhp


def xyxyp_to_cxywhp(xyxyp):
    cxywh = xyxy_to_cxywh(xyxyp)
    return cxywh


def xywhp_to_xyxyp(xywhp):
    xyxyp = xywh_to_xyxy(xywhp)
    return xyxyp


def xywhp_to_cxywhp(xywhp):
    cxywhp = xywh_to_cxywh(xywhp)
    return cxywhp


def cxywhp_to_xyxyp(cxywhp):
    xyxyp = cxywh_to_xyxy(cxywhp)
    return xyxyp


def cxywhp_to_xywhp(cxywhp):
    xywhp = cxywh_to_xywh(cxywhp)
    return xywhp
