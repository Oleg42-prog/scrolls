from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxy_to_xywhp(xyxy, original_size):
    xyxyp = coordinate_systems.original_to_percentaged(xyxy, original_size)
    xywhp = representations.xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxy_to_cxywhp(xyxy, original_size):
    xyxyp = coordinate_systems.original_to_percentaged(xyxy, original_size)
    cxywhp = representations.xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywh_to_xyxyp(xywh, original_size):
    xywhp = coordinate_systems.original_to_percentaged(xywh, original_size)
    xyxyp = representations.xywhp_to_xyxyp(xywhp)
    return xyxyp


def xywh_to_cxywhp(xywh, original_size):
    xywhp = coordinate_systems.original_to_percentaged(xywh, original_size)
    cxywhp = representations.xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywh_to_xyxyp(cxywh, original_size):
    cxywhp = coordinate_systems.original_to_percentaged(cxywh, original_size)
    xyxyp = representations.cxywhp_to_xyxyp(cxywhp)
    return xyxyp


def cxywh_to_xywhp(cxywh, original_size):
    cxywhp = coordinate_systems.original_to_percentaged(cxywh, original_size)
    xywhp = representations.cxywhp_to_xywhp(cxywhp)
    return xywhp
