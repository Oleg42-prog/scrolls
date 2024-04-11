from scrolls.geometry.boxes.convertors.simple import cxywhp_to_cxywh, xywhp_to_xywh, xyxyp_to_xyxy
from scrolls.geometry.boxes.convertors.representations import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations import cxywh_to_xyxy, cxywh_to_xywh


def xyxyp_to_xywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xyxyp_to_cxywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhp_to_xyxy(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def xywhp_to_cxywh(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def cxywhp_to_xyxy(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhp_to_xywh(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh
