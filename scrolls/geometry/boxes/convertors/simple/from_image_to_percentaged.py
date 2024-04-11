from scrolls.geometry.boxes.convertors.simple.from_image_to_normalized import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn


def xyxy_to_xyxyp(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywh_to_xywhp(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    xywhp = xywhn * 100
    return xywhp


def cxywh_to_cxywhp(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    cxywhp = cxywhn * 100
    return cxywhp
