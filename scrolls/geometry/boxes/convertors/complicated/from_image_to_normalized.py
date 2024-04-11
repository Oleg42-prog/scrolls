from scrolls.geometry.boxes.transforms import normalize_bounding_boxes
from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import cxywhn_to_xyxyn, cxywhn_to_xywhn


def xyxy_to_xywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def xyxy_to_cxywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywh_to_xyxyn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def xywh_to_cxywhn(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywh_to_xyxyn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywh_to_xywhn(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    xywhn = cxywhn_to_xywhn(cxywhn)
    return xywhn
