from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh, cxywh_to_xywh


def xyxy_to_xywhp():
    pass


def xywh_to_xywhp():
    pass


def xyxyn_to_xywhp():
    pass


def xywhn_to_xywhp(bounding_boxes):
    return bounding_boxes * 100


def cxywh_to_xywhp():
    pass


def cxywhn_to_xywhp():
    pass


def xyxyp_to_xywhp(bounding_boxes):
    return xyxy_to_xywh(bounding_boxes)


def xywhp_to_xywhp(bounding_boxes):
    return bounding_boxes


def cxywhp_to_xywhp(bounding_boxes):
    return cxywh_to_xywh(bounding_boxes)
