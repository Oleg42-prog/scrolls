from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def cxywhp_to_cxywh(cxywhp, original_size):
    cxywh = coordinate_systems.percentaged_to_original(cxywhp, original_size)
    return cxywh


@empty_array_return
def xywhp_to_xywh(xywhp, original_size):
    xywh = coordinate_systems.percentaged_to_original(xywhp, original_size)
    return xywh


@empty_array_return
def xyxyp_to_xyxy(xyxyp, original_size):
    xyxy = coordinate_systems.percentaged_to_original(xyxyp, original_size)
    return xyxy
