from scrolls.geometry.linal import carry_apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xyxy import xyxyn_to_xyxy, xyxyp_to_xyxy
from scrolls.geometry.boxes.to_cxywh import cxywhn_to_cxywh, cxywhp_to_cxywh


def xyxy_to_xywh(xyxy):
    _xyxy_to_xywh_transform = carry_apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ])
    return _xyxy_to_xywh_transform(xyxy)


def xywh_to_xywh(xywh):
    return xywh


def xyxyn_to_xywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    return xyxy_to_xywh(xyxy)


def xywhn_to_xywh(xywhn, image_size):
    return rescale_bounding_boxes(xywhn, image_size)


def cxywh_to_xywh(cxywh):
    _cxywh_to_xywh_transform = carry_apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return _cxywh_to_xywh_transform(cxywh)


def cxywhn_to_xywh(cxywhn, image_size):
    cxywh = cxywhn_to_cxywh(cxywhn, image_size)
    return cxywh_to_xywh(cxywh)


def xyxyp_to_xywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    return xyxy_to_xywh(xyxy)


def xywhp_to_xywh(xywhp, image_size):
    xywhn = xywhp / 100
    return rescale_bounding_boxes(xywhn, image_size)


def cxywhp_to_xywh(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    return cxywh_to_xywh(cxywh)
