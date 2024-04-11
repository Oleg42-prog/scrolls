from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxy_to_xywhn(xyxy, original_size):
    xyxyn = coordinate_systems.original_to_normalized(xyxy, original_size)
    xywhn = representations.xyxyn_to_xywhn(xyxyn)
    return xywhn


def xyxy_to_cxywhn(xyxy, original_size):
    xyxyn = coordinate_systems.original_to_normalized(xyxy, original_size)
    cxywhn = representations.xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywh_to_xyxyn(xywh, original_size):
    xywhn = coordinate_systems.original_to_normalized(xywh, original_size)
    xyxyn = representations.xywhn_to_xyxyn(xywhn)
    return xyxyn


def xywh_to_cxywhn(xywh, original_size):
    xywhn = coordinate_systems.original_to_normalized(xywh, original_size)
    cxywhn = representations.xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywh_to_xyxyn(cxywh, original_size):
    cxywhn = coordinate_systems.original_to_normalized(cxywh, original_size)
    xyxyn = representations.cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywh_to_xywhn(cxywh, original_size):
    cxywhn = coordinate_systems.original_to_normalized(cxywh, original_size)
    xywhn = representations.cxywhn_to_xywhn(cxywhn)
    return xywhn
