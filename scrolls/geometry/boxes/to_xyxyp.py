from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xywh_to_xyxyn, xywhn_to_xyxyn, cxywh_to_xyxyn, cxywhn_to_xyxyn


def xyxy_to_xyxyp(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywh_to_xyxyp(xywh, image_size):
    xyxyn = xywh_to_xyxyn(xywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xyxyn_to_xyxyp(xyxyn):
    xyxyp = xyxyn * 100
    return xyxyp


def xywhn_to_xyxyp(xywhn):
    xyxyn = xywhn_to_xyxyn(xywhn)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywh_to_xyxyp(cxywh, image_size):
    xyxyn = cxywh_to_xyxyn(cxywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywhn_to_xyxyp(cxywhn):
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    xyxyp = xyxyn * 100
    return xyxyp


def xyxyp_to_xyxyp(xyxyp):
    return xyxyp


def xywhp_to_xyxyp(xywhp):
    xyxyp = xywh_to_xyxy(xywhp)
    return xyxyp


def cxywhp_to_xyxyp(cxywhp):
    xyxyp = cxywh_to_xyxy(cxywhp)
    return xyxyp
