from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def cxywhn_to_cxywh(cxywhn, original_size):
    cxywh = coordinate_systems.normalized_to_original(cxywhn, original_size)
    return cxywh


@empty_array_return
def xywhn_to_xywh(xywhn, original_size):
    xywh = coordinate_systems.normalized_to_original(xywhn, original_size)
    return xywh


@empty_array_return
def xyxyn_to_xyxy(xyxyn, original_size):
    xyxy = coordinate_systems.normalized_to_original(xyxyn, original_size)
    return xyxy
