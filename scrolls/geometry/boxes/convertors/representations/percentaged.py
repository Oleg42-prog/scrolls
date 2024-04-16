from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh


@empty_array_return
def xyxyp_to_xywhp(xyxyp):
    xywhp = xyxy_to_xywh(xyxyp)
    return xywhp


@empty_array_return
def xyxyp_to_cxywhp(xyxyp):
    cxywh = xyxy_to_cxywh(xyxyp)
    return cxywh


@empty_array_return
def xywhp_to_xyxyp(xywhp):
    xyxyp = xywh_to_xyxy(xywhp)
    return xyxyp


@empty_array_return
def xywhp_to_cxywhp(xywhp):
    cxywhp = xywh_to_cxywh(xywhp)
    return cxywhp


@empty_array_return
def cxywhp_to_xyxyp(cxywhp):
    xyxyp = cxywh_to_xyxy(cxywhp)
    return xyxyp


@empty_array_return
def cxywhp_to_xywhp(cxywhp):
    xywhp = cxywh_to_xywh(cxywhp)
    return xywhp
