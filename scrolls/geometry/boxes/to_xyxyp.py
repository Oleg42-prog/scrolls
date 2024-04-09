from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xywh_to_xyxyn, xywhn_to_xyxyn, cxywh_to_xyxyn, cxywhn_to_xyxyn


def xyxy_to_xyxyp(xyxy, image_size):
    return xyxy_to_xyxyn(xyxy, image_size) * 100


def xywh_to_xyxyp(xywh, image_size):
    return xywh_to_xyxyn(xywh, image_size) * 100


def xyxyn_to_xyxyp(xyxyn):
    return xyxyn * 100


def xywhn_to_xyxyp(xywhn):
    return xywhn_to_xyxyn(xywhn) * 100


def cxywh_to_xyxyp(cxywh, image_size):
    return cxywh_to_xyxyn(cxywh, image_size) * 100


def cxywhn_to_xyxyp(cxywhn):
    return cxywhn_to_xyxyn(cxywhn) * 100


def xyxyp_to_xyxyp(xyxyp):
    return xyxyp


def xywhp_to_xyxyp(xywhp):
    return xywh_to_xyxy(xywhp)


def cxywhp_to_xyxyp(cxywhp):
    return cxywh_to_xyxy(cxywhp)
