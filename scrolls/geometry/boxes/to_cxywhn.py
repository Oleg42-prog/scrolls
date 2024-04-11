from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xyxyp_to_xyxyn
from scrolls.geometry.boxes.to_xywhn import xywh_to_xywhn, xywhp_to_xywhn


def xyxy_to_cxywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywh_to_cxywhn(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


from scrolls.geometry.boxes.convertors.synonyms import xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms import xywhn_to_cxywhn


def cxywh_to_cxywhn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    return cxywhn


from scrolls.geometry.boxes.convertors.identity import cxywhn_to_cxywhn


def xyxyp_to_cxywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywhp_to_cxywhn(xywhp):
    xywhn = xywhp_to_xywhn(xywhp)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywhp_to_cxywhn(cxywhp):
    cxywhn = cxywhp / 100
    return cxywhn
