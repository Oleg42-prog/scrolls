from scrolls.geometry.boxes.transforms import normalize_bounding_boxes

from scrolls.geometry.boxes.convertors.to_normalised import xyxy_to_xyxyn


def xywh_to_xyxyn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


from scrolls.geometry.boxes.convertors.identity import xyxyn_to_xyxyn
from scrolls.geometry.boxes.convertors.synonyms import xywhn_to_xyxyn


def cxywh_to_xyxyn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


from scrolls.geometry.boxes.convertors.synonyms import cxywhn_to_xyxyn
from scrolls.geometry.boxes.convertors.to_normalised import xyxyp_to_xyxyn


def xywhp_to_xyxyn(xywhp):
    xywhn = xywhp / 100
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = cxywhp / 100
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn
