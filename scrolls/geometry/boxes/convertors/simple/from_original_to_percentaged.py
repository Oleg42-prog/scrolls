from scrolls.geometry.boxes.convertors import coordinate_systems


def xyxy_to_xyxyp(xyxy, original_size):
    xyxyp = coordinate_systems.original_to_percentaged(xyxy, original_size)
    return xyxyp


def xywh_to_xywhp(xywh, original_size):
    xywhp = coordinate_systems.original_to_percentaged(xywh, original_size)
    return xywhp


def cxywh_to_cxywhp(cxywh, original_size):
    cxywhp = coordinate_systems.original_to_percentaged(cxywh, original_size)
    return cxywhp
