from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def xyxyn_to_xyxyp(xyxyn):
    xyxyp = coordinate_systems.normalized_to_percentaged(xyxyn)
    return xyxyp


@empty_array_return
def xywhn_to_xywhp(xywhn):
    xywhp = coordinate_systems.normalized_to_percentaged(xywhn)
    return xywhp


@empty_array_return
def cxywhn_to_cxywhp(cxywhn):
    cxywhp = coordinate_systems.normalized_to_percentaged(cxywhn)
    return cxywhp
