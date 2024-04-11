from scrolls.geometry.boxes.to_xyxyp import xyxy_to_xyxyp, xyxyn_to_xyxyp
from scrolls.geometry.boxes.to_xywhp import xywh_to_xywhp, xywhn_to_xywhp
from scrolls.geometry.boxes.to_cxywhn import cxywh_to_cxywhn


def xyxy_to_cxywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywh_to_cxywhp(xywh, image_size):
    xywhp = xywh_to_xywhp(xywh, image_size)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def xyxyn_to_cxywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywhn_to_cxywhp(xywhn):
    xywhp = xywhn_to_xywhp(xywhn)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywh_to_cxywhp(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    cxywhp = cxywhn * 100
    return cxywhp


def cxywhn_to_cxywhp(cxywhn):
    cxywhp = cxywhn * 100
    return cxywhp


from scrolls.geometry.boxes.convertors.synonyms import xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms import xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.identity import cxywhp_to_cxywhp
