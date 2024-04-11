from scrolls.geometry.boxes.transforms import rescale_bounding_boxes


def cxywhp_to_cxywh(cxywhp, original_size):
    cxywhn = cxywhp / 100
    cxywh = rescale_bounding_boxes(cxywhn, original_size)
    return cxywh


def xywhp_to_xywh(xywhp, original_size):
    xywhn = xywhp / 100
    xywh = rescale_bounding_boxes(xywhn, original_size)
    return xywh


def xyxyp_to_xyxy(xyxyp, original_size):
    xyxyn = xyxyp / 100
    xyxy = rescale_bounding_boxes(xyxyn, original_size)
    return xyxy
