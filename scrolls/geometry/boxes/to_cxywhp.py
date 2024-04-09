from scrolls.geometry.boxes.to_cxywh import xyxy_to_cxywh, xywh_to_cxywh


def xyxy_to_cxywhp():
    pass


def xywh_to_cxywhp():
    pass


def xyxyn_to_cxywhp():
    pass


def xywhn_to_cxywhp():
    pass


def cxywh_to_cxywhp():
    pass


def cxywhn_to_cxywhp(bounding_boxes):
    return bounding_boxes * 100


def xyxyp_to_cxywhp(bounding_boxes):
    return xyxy_to_cxywh(bounding_boxes)


def xywhp_to_cxywhp(bounding_boxes):
    return xywh_to_cxywh(bounding_boxes)


def cxywhp_to_cxywhp(bounding_boxes):
    return bounding_boxes
