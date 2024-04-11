from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xywh import xywhp_to_xywh
from scrolls.geometry.boxes.to_cxywh import cxywhp_to_cxywh


from scrolls.geometry.boxes.convertors.identity import xyxy_to_xyxy
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy
from scrolls.geometry.boxes.convertors.from_normalised import xyxyn_to_xyxy


def xywhn_to_xyxy(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy


def cxywhn_to_xyxy(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


from scrolls.geometry.boxes.convertors.from_percentaged import xyxyp_to_xyxy


def xywhp_to_xyxy(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def cxywhp_to_xyxy(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy
