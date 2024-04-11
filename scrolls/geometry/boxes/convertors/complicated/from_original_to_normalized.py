from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import cxywhn_to_xyxyn, cxywhn_to_xywhn


def xyxy_to_xywhn(xyxy, original_size):
    xyxyn = xyxy_to_xyxyn(xyxy, original_size)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def xyxy_to_cxywhn(xyxy, original_size):
    xyxyn = xyxy_to_xyxyn(xyxy, original_size)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywh_to_xyxyn(xywh, original_size):
    xywhn = normalize_bounding_boxes(xywh, original_size)
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def xywh_to_cxywhn(xywh, original_size):
    xywhn = xywh_to_xywhn(xywh, original_size)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywh_to_xyxyn(cxywh, original_size):
    cxywhn = normalize_bounding_boxes(cxywh, original_size)
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywh_to_xywhn(cxywh, original_size):
    cxywhn = cxywh_to_cxywhn(cxywh, original_size)
    xywhn = cxywhn_to_xywhn(cxywhn)
    return xywhn
