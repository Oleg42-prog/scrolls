from scrolls.geometry.boxes.convertors.representation import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy, cxywh_to_xywh


def xyxyn_to_xywhn(xyxyn):
    xywhn = xyxy_to_xywh(xyxyn)
    return xywhn


def xyxyn_to_cxywhn(xyxyn):
    cxywhn = xyxy_to_cxywh(xyxyn)
    return cxywhn


def xywhn_to_xyxyn(xywhn):
    xyxyn = xywh_to_xyxy(xywhn)
    return xyxyn


def xywhn_to_cxywhn(xywhn):
    cxywhn = xywh_to_cxywh(xywhn)
    return cxywhn


def cxywhn_to_xyxyn(cxywhn):
    xyxyn = cxywh_to_xyxy(cxywhn)
    return xyxyn


def cxywhn_to_xywhn(cxywhn):
    xywhn = cxywh_to_xywh(cxywhn)
    return xywhn
