from scrolls.geometry.boxes.convertors.simple import cxywhp_to_cxywh, xywhp_to_xywh, xyxyp_to_xyxy
from scrolls.geometry.boxes.convertors.representations import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations import cxywh_to_xyxy, cxywh_to_xywh


def xyxyp_to_xywh(xyxyp, original_size):
    xyxy = xyxyp_to_xyxy(xyxyp, original_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xyxyp_to_cxywh(xyxyp, original_size):
    xyxy = xyxyp_to_xyxy(xyxyp, original_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhp_to_xyxy(xywhp, original_size):
    xywh = xywhp_to_xywh(xywhp, original_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def xywhp_to_cxywh(xywhp, original_size):
    xywh = xywhp_to_xywh(xywhp, original_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def cxywhp_to_xyxy(cxywhp, original_size):
    cxywh = cxywhp_to_cxywh(cxywhp, original_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhp_to_xywh(cxywhp, original_size):
    cxywh = cxywhp_to_cxywh(cxywhp, original_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh
