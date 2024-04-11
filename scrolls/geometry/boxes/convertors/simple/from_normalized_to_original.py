from scrolls.geometry.boxes.convertors import coordinate_systems


def cxywhn_to_cxywh(cxywhn, original_size):
    cxywh = coordinate_systems.normalized_to_original(cxywhn, original_size)
    return cxywh


def xywhn_to_xywh(xywhn, original_size):
    xywh = coordinate_systems.normalized_to_original(xywhn, original_size)
    return xywh


def xyxyn_to_xyxy(xyxyn, original_size):
    xyxy = coordinate_systems.normalized_to_original(xyxyn, original_size)
    return xyxy
