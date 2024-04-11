from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyp, xywh_to_xywhp, cxywh_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import cxywhp_to_xywhp
from scrolls.geometry.boxes.convertors.complicated.from_image_to_normalized import xywh_to_xyxyn, cxywh_to_xyxyn


def xyxy_to_xywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxy_to_cxywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywh_to_xyxyp(xywh, image_size):
    xyxyn = xywh_to_xyxyn(xywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywh_to_cxywhp(xywh, image_size):
    xywhp = xywh_to_xywhp(xywh, image_size)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywh_to_xyxyp(cxywh, image_size):
    xyxyn = cxywh_to_xyxyn(cxywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywh_to_xywhp(cxywh, image_size):
    cxywhp = cxywh_to_cxywhp(cxywh, image_size)
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp
