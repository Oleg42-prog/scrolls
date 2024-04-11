from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.convertors.from_normalised import cxywhn_to_cxywh, xywhn_to_xywh, xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.representation import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy, cxywh_to_xywh


def xyxyn_to_xywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xyxyn_to_cxywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhn_to_xyxy(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def xywhn_to_cxywh(xywhn, image_size):
    xywh = xywhn_to_xywh(xywhn, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def cxywhn_to_xyxy(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhn_to_xywh(cxywhn, image_size):
    cxywh = cxywhn_to_cxywh(cxywhn, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh