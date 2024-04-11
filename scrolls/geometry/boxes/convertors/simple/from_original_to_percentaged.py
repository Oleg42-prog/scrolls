from scrolls.geometry.boxes.convertors.simple.from_original_to_normalized import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn


def xyxy_to_xyxyp(xyxy, original_size):
    xyxyn = xyxy_to_xyxyn(xyxy, original_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywh_to_xywhp(xywh, original_size):
    xywhn = xywh_to_xywhn(xywh, original_size)
    xywhp = xywhn * 100
    return xywhp


def cxywh_to_cxywhp(cxywh, original_size):
    cxywhn = cxywh_to_cxywhn(cxywh, original_size)
    cxywhp = cxywhn * 100
    return cxywhp
