from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxyp_to_xywh(xyxyp, original_size):
    xyxy = coordinate_systems.percentaged_to_original(xyxyp, original_size)
    xywh = representations.xyxy_to_xywh(xyxy)
    return xywh


def xyxyp_to_cxywh(xyxyp, original_size):
    xyxy = coordinate_systems.percentaged_to_original(xyxyp, original_size)
    cxywh = representations.xyxy_to_cxywh(xyxy)
    return cxywh


def xywhp_to_xyxy(xywhp, original_size):
    xywh = coordinate_systems.percentaged_to_original(xywhp, original_size)
    xyxy = representations.xywh_to_xyxy(xywh)
    return xyxy


def xywhp_to_cxywh(xywhp, original_size):
    xywh = coordinate_systems.percentaged_to_original(xywhp, original_size)
    cxywh = representations.xywh_to_cxywh(xywh)
    return cxywh


def cxywhp_to_xyxy(cxywhp, original_size):
    cxywh = coordinate_systems.percentaged_to_original(cxywhp, original_size)
    xyxy = representations.cxywh_to_xyxy(cxywh)
    return xyxy


def cxywhp_to_xywh(cxywhp, original_size):
    cxywh = coordinate_systems.percentaged_to_original(cxywhp, original_size)
    xywh = representations.cxywh_to_xywh(cxywh)
    return xywh
