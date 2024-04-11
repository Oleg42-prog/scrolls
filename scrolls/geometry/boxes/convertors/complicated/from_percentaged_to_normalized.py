from scrolls.geometry.boxes.convertors.simple import xyxyp_to_xyxyn, xywhp_to_xywhn, cxywhp_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import cxywhn_to_xyxyn, cxywhn_to_xywhn


def xyxyp_to_xywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def xyxyp_to_cxywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywhp_to_xyxyn(xywhp):
    xywhn = xywhp / 100
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def xywhp_to_cxywhn(xywhp):
    xywhn = xywhp_to_xywhn(xywhp)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = cxywhp / 100
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywhp_to_xywhn(cxywhp):
    cxywhp = cxywhp_to_cxywhn(cxywhp)
    xywhn = cxywhn_to_xywhn(cxywhp)
    return xywhn
