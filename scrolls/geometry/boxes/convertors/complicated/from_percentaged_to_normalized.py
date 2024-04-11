from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxyp_to_xywhn(xyxyp):
    xyxyn = coordinate_systems.percentaged_to_normalized(xyxyp)
    xywhn = representations.xyxyn_to_xywhn(xyxyn)
    return xywhn


def xyxyp_to_cxywhn(xyxyp):
    xyxyn = coordinate_systems.percentaged_to_normalized(xyxyp)
    cxywhn = representations.xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywhp_to_xyxyn(xywhp):
    xywhn = coordinate_systems.percentaged_to_normalized(xywhp)
    xyxyn = representations.xywhn_to_xyxyn(xywhn)
    return xyxyn


def xywhp_to_cxywhn(xywhp):
    xywhn = coordinate_systems.percentaged_to_normalized(xywhp)
    cxywhn = representations.xywhn_to_cxywhn(xywhn)
    return cxywhn


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = coordinate_systems.percentaged_to_normalized(cxywhp)
    xyxyn = representations.cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def cxywhp_to_xywhn(cxywhp):
    cxywhp = coordinate_systems.percentaged_to_normalized(cxywhp)
    xywhn = representations.cxywhn_to_xywhn(cxywhp)
    return xywhn
