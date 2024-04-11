from scrolls.geometry.boxes.transforms import rescale_bounding_boxes


def cxywhp_to_cxywh(cxywhp, image_size):
    cxywhn = cxywhp / 100
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    return cxywh


def xywhp_to_xywh(xywhp, image_size):
    xywhn = xywhp / 100
    xywh = rescale_bounding_boxes(xywhn, image_size)
    return xywh


def xyxyp_to_xyxy(xyxyp, image_size):
    xyxyn = xyxyp / 100
    xyxy = rescale_bounding_boxes(xyxyn, image_size)
    return xyxy
