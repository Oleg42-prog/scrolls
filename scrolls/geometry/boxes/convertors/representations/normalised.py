from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh


@empty_array_return
def xyxyn_to_xywhn(xyxyn):
    xywhn = xyxy_to_xywh(xyxyn)
    return xywhn


@empty_array_return
def xyxyn_to_cxywhn(xyxyn):
    cxywhn = xyxy_to_cxywh(xyxyn)
    return cxywhn


@empty_array_return
def xywhn_to_xyxyn(xywhn):
    xyxyn = xywh_to_xyxy(xywhn)
    return xyxyn


@empty_array_return
def xywhn_to_cxywhn(xywhn):
    cxywhn = xywh_to_cxywh(xywhn)
    return cxywhn


@empty_array_return
def cxywhn_to_xyxyn(cxywhn):
    xyxyn = cxywh_to_xyxy(cxywhn)
    return xyxyn


@empty_array_return
def cxywhn_to_xywhn(cxywhn):
    xywhn = cxywh_to_xywh(cxywhn)
    return xywhn
