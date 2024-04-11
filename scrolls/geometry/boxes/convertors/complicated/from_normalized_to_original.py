from scrolls.geometry.boxes.convertors.simple import cxywhn_to_cxywh, xywhn_to_xywh, xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.representations import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations import cxywh_to_xyxy, cxywh_to_xywh


def xyxyn_to_xywh(xyxyn, original_size):
    xyxy = xyxyn_to_xyxy(xyxyn, original_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xyxyn_to_cxywh(xyxyn, original_size):
    xyxy = xyxyn_to_xyxy(xyxyn, original_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhn_to_xyxy(xywhn, original_size):
    xywh = xywhn_to_xywh(xywhn, original_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def xywhn_to_cxywh(xywhn, original_size):
    xywh = xywhn_to_xywh(xywhn, original_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def cxywhn_to_xyxy(cxywhn, original_size):
    cxywh = cxywhn_to_cxywh(cxywhn, original_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhn_to_xywh(cxywhn, original_size):
    cxywh = cxywhn_to_cxywh(cxywhn, original_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh
