from scrolls.geometry.boxes.transforms import rescale_bounding_boxes


def cxywhn_to_cxywh(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    return cxywh


def xywhn_to_xywh(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    return xywh


def xyxyn_to_xyxy(xyxyn, image_size):
    xyxy = rescale_bounding_boxes(xyxyn, image_size)
    return xyxy
