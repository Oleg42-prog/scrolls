from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyp, xywh_to_xywhp, cxywh_to_cxywhp
from scrolls.geometry.boxes.convertors.representations import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations import xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations import cxywhp_to_xywhp
from scrolls.geometry.boxes.convertors.complicated.from_original_to_normalized import xywh_to_xyxyn, cxywh_to_xyxyn


def xyxy_to_xywhp(xyxy, original_size):
    xyxyp = xyxy_to_xyxyp(xyxy, original_size)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxy_to_cxywhp(xyxy, original_size):
    xyxyp = xyxy_to_xyxyp(xyxy, original_size)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywh_to_xyxyp(xywh, original_size):
    xyxyn = xywh_to_xyxyn(xywh, original_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywh_to_cxywhp(xywh, original_size):
    xywhp = xywh_to_xywhp(xywh, original_size)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywh_to_xyxyp(cxywh, original_size):
    xyxyn = cxywh_to_xyxyn(cxywh, original_size)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywh_to_xywhp(cxywh, original_size):
    cxywhp = cxywh_to_cxywhp(cxywh, original_size)
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp
