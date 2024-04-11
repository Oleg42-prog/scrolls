from scrolls.geometry.boxes.transforms import normalize_bounding_boxes


def xyxy_to_xyxyn(xyxy, original_size):
    xyxyn = normalize_bounding_boxes(xyxy, original_size)
    return xyxyn


def xywh_to_xywhn(xywh, original_size):
    xywhn = normalize_bounding_boxes(xywh, original_size)
    return xywhn


def cxywh_to_cxywhn(cxywh, original_size):
    cxywhn = normalize_bounding_boxes(cxywh, original_size)
    return cxywhn
