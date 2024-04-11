from scrolls.geometry.boxes.convertors.simple.from_percentaged_to_normalized import xyxyp_to_xyxyn
from scrolls.geometry.boxes.convertors.simple.from_percentaged_to_normalized import xywhp_to_xywhn
from scrolls.geometry.boxes.convertors.simple.from_percentaged_to_normalized import cxywhp_to_cxywhn

from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import xywhn_to_xywh
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import cxywhn_to_cxywh


def cxywhp_to_cxywh(cxywhp, original_size):
    cxywhn = cxywhp_to_cxywhn(cxywhp)
    cxywh = cxywhn_to_cxywh(cxywhn, original_size)
    return cxywh


def xywhp_to_xywh(xywhp, original_size):
    xywhn = xywhp_to_xywhn(xywhp)
    xywh = xywhn_to_xywh(xywhn, original_size)
    return xywh


def xyxyp_to_xyxy(xyxyp, original_size):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    xyxy = xyxyn_to_xyxy(xyxyn, original_size)
    return xyxy
