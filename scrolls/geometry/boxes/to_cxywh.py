from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy, xyxyp_to_xyxy
from scrolls.geometry.boxes.to_xywh import xywhn_to_xywh, xywhp_to_xywh


from scrolls.geometry.boxes.convertors.representation import xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representation import xywh_to_cxywh


def xyxyn_to_cxywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhn_to_cxywh(xywhn, image_size):
    xywh = xywhn_to_xywh(xywhn, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


from scrolls.geometry.boxes.convertors.identity import cxywh_to_cxywh


def cxywhn_to_cxywh(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    return cxywh


def xyxyp_to_cxywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhp_to_cxywh(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def cxywhp_to_cxywh(cxywhp, image_size):
    cxywhn = cxywhp / 100
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    return cxywh
