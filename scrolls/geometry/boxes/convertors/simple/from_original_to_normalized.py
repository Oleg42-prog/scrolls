from scrolls.geometry.boxes.convertors import coordinate_systems


def xyxy_to_xyxyn(xyxy, original_size):
    xyxyn = coordinate_systems.original_to_normalized(xyxy, original_size)
    return xyxyn


def xywh_to_xywhn(xywh, original_size):
    xywhn = coordinate_systems.original_to_normalized(xywh, original_size)
    return xywhn


def cxywh_to_cxywhn(cxywh, original_size):
    cxywhn = coordinate_systems.original_to_normalized(cxywh, original_size)
    return cxywhn
