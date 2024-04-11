from scrolls.geometry.boxes.convertors.simple import xyxyn_to_xyxyp, xywhn_to_xywhp
from scrolls.geometry.boxes.convertors.synonyms.normalised import xywhn_to_xyxyn
from scrolls.geometry.boxes.convertors.synonyms.normalised import cxywhn_to_xyxyn
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import cxywhp_to_xywhp


def xyxyn_to_xywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxyn_to_cxywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywhn_to_xyxyp(xywhn):
    xyxyn = xywhn_to_xyxyn(xywhn)
    xyxyp = xyxyn * 100
    return xyxyp


def xywhn_to_cxywhp(xywhn):
    xywhp = xywhn_to_xywhp(xywhn)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywhn_to_xyxyp(cxywhn):
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywhn_to_xywhp(cxywhn):
    cxywhp = cxywhn * 100
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp
