from scrolls.geometry.linal import apply_linear_operator


def xyxy_to_xywh(xyxy):
    xywh = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ], xyxy)
    return xywh


def xywh_to_xyxy(xywh):
    xyxy = apply_linear_operator([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ], xywh)
    return xyxy


def xyxy_to_cxywh(xyxy):
    cxywh = apply_linear_operator([
        [0.5, 0, 0.5, 0],
        [0, 0.5, 0.5, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1]
    ], xyxy)
    return cxywh


def xywh_to_cxywh(xywh):
    cxywh = apply_linear_operator([
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], xywh)
    return cxywh


def cxywh_to_xyxy(cxywh):
    xyxy = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5]
    ], cxywh)
    return xyxy


def cxywh_to_xywh(cxywh):
    xywh = apply_linear_operator([
        [1, 0, -0.5, 0],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], cxywh)
    return xywh
