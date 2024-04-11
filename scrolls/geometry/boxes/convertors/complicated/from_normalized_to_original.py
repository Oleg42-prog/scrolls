from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxyn_to_xywh(xyxyn, original_size):
    xyxy = coordinate_systems.normalized_to_original(xyxyn, original_size)
    xywh = representations.xyxy_to_xywh(xyxy)
    return xywh


def xyxyn_to_cxywh(xyxyn, original_size):
    xyxy = coordinate_systems.normalized_to_original(xyxyn, original_size)
    cxywh = representations.xyxy_to_cxywh(xyxy)
    return cxywh


def xywhn_to_xyxy(xywhn, original_size):
    xywh = coordinate_systems.normalized_to_original(xywhn, original_size)
    xyxy = representations.xywh_to_xyxy(xywh)
    return xyxy


def xywhn_to_cxywh(xywhn, original_size):
    xywh = coordinate_systems.normalized_to_original(xywhn, original_size)
    cxywh = representations.xywh_to_cxywh(xywh)
    return cxywh


def cxywhn_to_xyxy(cxywhn, original_size):
    cxywh = coordinate_systems.normalized_to_original(cxywhn, original_size)
    xyxy = representations.cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhn_to_xywh(cxywhn, original_size):
    cxywh = coordinate_systems.normalized_to_original(cxywhn, original_size)
    xywh = representations.cxywh_to_xywh(cxywh)
    return xywh
