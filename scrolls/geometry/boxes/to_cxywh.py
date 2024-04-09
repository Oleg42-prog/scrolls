from scrolls.geometry.linal import carry_apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy, xyxyp_to_xyxy
from scrolls.geometry.boxes.to_xywh import xywhn_to_xywh, xywhp_to_xywh


def xyxy_to_cxywh(xyxy):
    _xyxy_to_cxywh_transform = carry_apply_linear_operator([
        [0.5, 0, 0.5, 0],
        [0, 0.5, 0.5, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ])
    return _xyxy_to_cxywh_transform(xyxy)


def xywh_to_cxywh(xywh):
    _xywh_to_cxywh_transform = carry_apply_linear_operator([
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return _xywh_to_cxywh_transform(xywh)


def xyxyn_to_cxywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    return xyxy_to_cxywh(xyxy)


def xywhn_to_cxywh(xywhn, image_size):
    xywh = xywhn_to_xywh(xywhn, image_size)
    return xywh_to_cxywh(xywh)


def cxywh_to_cxywh(cxywh):
    return cxywh


def cxywhn_to_cxywh(cxywhn, image_size):
    return rescale_bounding_boxes(cxywhn, image_size)


def xyxyp_to_cxywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    return xyxy_to_cxywh(xyxy)


def xywhp_to_cxywh(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    return xywh_to_cxywh(xywh)


def cxywhp_to_cxywh(cxywhp, image_size):
    cxywhn = cxywhp / 100
    return rescale_bounding_boxes(cxywhn, image_size)
