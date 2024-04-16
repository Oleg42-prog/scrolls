from scrolls.geometry.decorators import empty_array_return
from scrolls.geometry.boxes.convertors import coordinate_systems


@empty_array_return
def xyxyp_to_xyxyn(xyxyp):
    xyxyn = coordinate_systems.percentaged_to_normalized(xyxyp)
    return xyxyn


@empty_array_return
def xywhp_to_xywhn(xywhp):
    xywhn = coordinate_systems.percentaged_to_normalized(xywhp)
    return xywhn


@empty_array_return
def cxywhp_to_cxywhn(cxywhp):
    cxywhn = coordinate_systems.percentaged_to_normalized(cxywhp)
    return cxywhn
