from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def xyxy_to_xyxyn(xyxy, original_size):
    xyxyn = coordinate_systems.original_to_normalized(xyxy, original_size)
    return xyxyn


@empty_array_return
def xywh_to_xywhn(xywh, original_size):
    xywhn = coordinate_systems.original_to_normalized(xywh, original_size)
    return xywhn


@empty_array_return
def cxywh_to_cxywhn(cxywh, original_size):
    cxywhn = coordinate_systems.original_to_normalized(cxywh, original_size)
    return cxywhn
