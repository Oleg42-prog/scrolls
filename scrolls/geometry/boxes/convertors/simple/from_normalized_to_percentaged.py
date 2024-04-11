from scrolls.geometry.boxes.convertors import coordinate_systems


def xyxyn_to_xyxyp(xyxyn):
    xyxyp = coordinate_systems.normalized_to_percentaged(xyxyn)
    return xyxyp


def xywhn_to_xywhp(xywhn):
    xywhp = coordinate_systems.normalized_to_percentaged(xywhn)
    return xywhp


def cxywhn_to_cxywhp(cxywhn):
    cxywhp = coordinate_systems.normalized_to_percentaged(cxywhn)
    return cxywhp
