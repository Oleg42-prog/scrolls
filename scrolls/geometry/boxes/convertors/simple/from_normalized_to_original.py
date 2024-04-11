from scrolls.geometry.boxes.transforms import rescale_bounding_boxes


def cxywhn_to_cxywh(cxywhn, original_size):
    cxywh = rescale_bounding_boxes(cxywhn, original_size)
    return cxywh


def xywhn_to_xywh(xywhn, original_size):
    xywh = rescale_bounding_boxes(xywhn, original_size)
    return xywh


def xyxyn_to_xyxy(xyxyn, original_size):
    xyxy = rescale_bounding_boxes(xyxyn, original_size)
    return xyxy
