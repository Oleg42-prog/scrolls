from scrolls.geometry.boxes.convertors import coordinate_systems
from scrolls.geometry.boxes.convertors import representations


def xyxyn_to_xywhp(xyxyn):
    xyxyp = coordinate_systems.normalized_to_percentaged(xyxyn)
    xywhp = representations.xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxyn_to_cxywhp(xyxyn):
    xyxyp = coordinate_systems.normalized_to_percentaged(xyxyn)
    cxywhp = representations.xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywhn_to_xyxyp(xywhn):
    xywhp = coordinate_systems.normalized_to_percentaged(xywhn)
    xyxyp = representations.xywhp_to_xyxyp(xywhp)
    return xyxyp


def xywhn_to_cxywhp(xywhn):
    xywhp = coordinate_systems.normalized_to_percentaged(xywhn)
    cxywhp = representations.xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywhn_to_xyxyp(cxywhn):
    cxywhp = coordinate_systems.normalized_to_percentaged(cxywhn)
    xyxyp = representations.cxywhp_to_xyxyp(cxywhp)
    return xyxyp


def cxywhn_to_xywhp(cxywhn):
    cxywhp = coordinate_systems.normalized_to_percentaged(cxywhn)
    xywhp = representations.cxywhp_to_xywhp(cxywhp)
    return xywhp
