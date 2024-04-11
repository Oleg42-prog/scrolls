from scrolls.geometry.boxes.transforms import normalize_bounding_boxes


def xyxy_to_xyxyn(xyxy, image_size):
    xyxyn = normalize_bounding_boxes(xyxy, image_size)
    return xyxyn


def xywh_to_xywhn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    return xywhn


def cxywh_to_cxywhn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    return cxywhn


def xyxyp_to_xyxyn(xyxyp):
    xyxyn = xyxyp / 100
    return xyxyn


def xywhp_to_xywhn(xywhp):
    xywhn = xywhp / 100
    return xywhn


def cxywhp_to_cxywhn(cxywhp):
    cxywhn = cxywhp / 100
    return cxywhn
