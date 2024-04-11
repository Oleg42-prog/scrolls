from scrolls.geometry.boxes.convertors import coordinate_systems


def xyxyp_to_xyxyn(xyxyp):
    xyxyn = coordinate_systems.percentaged_to_normalized(xyxyp)
    return xyxyn


def xywhp_to_xywhn(xywhp):
    xywhn = coordinate_systems.percentaged_to_normalized(xywhp)
    return xywhn


def cxywhp_to_cxywhn(cxywhp):
    cxywhn = coordinate_systems.percentaged_to_normalized(cxywhp)
    return cxywhn
