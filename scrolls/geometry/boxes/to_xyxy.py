from scrolls.geometry.linal import apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xywh import xywhp_to_xywh
from scrolls.geometry.boxes.to_cxywh import cxywhp_to_cxywh


from scrolls.geometry.boxes.convertors.identity import xyxy_to_xyxy


def xywh_to_xyxy(xywh):
    xyxy = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ], xywh)
    return xyxy


def xyxyn_to_xyxy(xyxyn, image_size):
    xyxy = rescale_bounding_boxes(xyxyn, image_size)
    return xyxy


def xywhn_to_xyxy(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def cxywh_to_xyxy(cxywh):
    xyxy = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5]
    ], cxywh)
    return xyxy


def cxywhn_to_xyxy(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def xyxyp_to_xyxy(xyxyp, image_size):
    xyxyn = xyxyp / 100
    xyxy = rescale_bounding_boxes(xyxyn, image_size)
    return xyxy


def xywhp_to_xyxy(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def cxywhp_to_xyxy(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy
