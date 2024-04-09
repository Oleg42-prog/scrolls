from scrolls.geometry.linal import carry_apply_linear_operator
from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xywh import xywhp_to_xywh
from scrolls.geometry.boxes.to_cxywh import cxywhp_to_cxywh


def xyxy_to_xyxy(xyxy):
    return xyxy


def xywh_to_xyxy(xywh):
    _xywh_to_xyxy_transform = carry_apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ])
    return _xywh_to_xyxy_transform(xywh)


def xyxyn_to_xyxy(xyxyn, image_size):
    return rescale_bounding_boxes(xyxyn, image_size)


def xywhn_to_xyxy(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    return xywh_to_xyxy(xywh)


def cxywh_to_xyxy(cxywh):
    _cxywh_to_xyxy_transform = carry_apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5]
    ])
    return _cxywh_to_xyxy_transform(cxywh)


def cxywhn_to_xyxy(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    return cxywh_to_xyxy(cxywh)


def xyxyp_to_xyxy(xyxyp, image_size):
    xyxyn = xyxyp / 100
    return rescale_bounding_boxes(xyxyn, image_size)


def xywhp_to_xyxy(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    return xywh_to_xyxy(xywh)


def cxywhp_to_xyxy(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    return cxywh_to_xyxy(cxywh)
