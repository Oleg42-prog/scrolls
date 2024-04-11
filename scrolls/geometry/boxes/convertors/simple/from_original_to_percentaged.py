from scrolls.geometry.boxes.convertors.simple.from_original_to_normalized import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_percentaged import xyxyn_to_xyxyp
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_percentaged import xywhn_to_xywhp
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_percentaged import cxywhn_to_cxywhp


def xyxy_to_xyxyp(xyxy, original_size):
    xyxyn = xyxy_to_xyxyn(xyxy, original_size)
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    return xyxyp


def xywh_to_xywhp(xywh, original_size):
    xywhn = xywh_to_xywhn(xywh, original_size)
    xywhp = xywhn_to_xywhp(xywhn)
    return xywhp


def cxywh_to_cxywhp(cxywh, original_size):
    cxywhn = cxywh_to_cxywhn(cxywh, original_size)
    cxywhp = cxywhn_to_cxywhp(cxywhn)
    return cxywhp
