from scrolls.geometry.linal import apply_linear_operator
from scrolls.geometry.decorators import empty_array_return


@empty_array_return
def xyxy_to_xywh(xyxy):
    xywh = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ], xyxy)
    return xywh


@empty_array_return
def xyxy_to_cxywh(xyxy):
    cxywh = apply_linear_operator([
        [0.5, 0, 0.5, 0],
        [0, 0.5, 0, 0.5],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ], xyxy)
    return cxywh


@empty_array_return
def xywh_to_xyxy(xywh):
    xyxy = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ], xywh)
    return xyxy


@empty_array_return
def xywh_to_cxywh(xywh):
    cxywh = apply_linear_operator([
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], xywh)
    return cxywh


@empty_array_return
def cxywh_to_xyxy(cxywh):
    xyxy = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5]
    ], cxywh)
    return xyxy


@empty_array_return
def cxywh_to_xywh(cxywh):
    xywh = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], cxywh)
    return xywh
