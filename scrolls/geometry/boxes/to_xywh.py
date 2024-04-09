from scrolls.geometry.linal import apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy, xyxyp_to_xyxy
from scrolls.geometry.boxes.to_cxywh import cxywhn_to_cxywh, cxywhp_to_cxywh


def xyxy_to_xywh(xyxy):
    xywh = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ], xyxy)
    return xywh


def xywh_to_xywh(xywh):
    return xywh


def xyxyn_to_xywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xywhn_to_xywh(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    return xywh


def cxywh_to_xywh(cxywh):
    xywh = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], cxywh)
    return xywh


def cxywhn_to_xywh(cxywhn, image_size):
    cxywh = cxywhn_to_cxywh(cxywhn, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh


def xyxyp_to_xywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xywhp_to_xywh(xywhp, image_size):
    xywhn = xywhp / 100
    xywh = rescale_bounding_boxes(xywhn, image_size)
    return xywh


def cxywhp_to_xywh(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh
