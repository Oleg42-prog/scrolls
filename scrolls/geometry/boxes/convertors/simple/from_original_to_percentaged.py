from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def xyxy_to_xyxyp(xyxy, original_size):
    xyxyp = coordinate_systems.original_to_percentaged(xyxy, original_size)
    return xyxyp


@empty_array_return
def xywh_to_xywhp(xywh, original_size):
    xywhp = coordinate_systems.original_to_percentaged(xywh, original_size)
    return xywhp


@empty_array_return
def cxywh_to_cxywhp(cxywh, original_size):
    cxywhp = coordinate_systems.original_to_percentaged(cxywh, original_size)
    return cxywhp
