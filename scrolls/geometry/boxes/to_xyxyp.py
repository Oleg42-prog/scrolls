from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy


def xyxy_to_xyxyp():
    pass


def xywh_to_xyxyp():
    pass


def xyxyn_to_xyxyp(bounding_boxes):
    return bounding_boxes * 100


def xywhn_to_xyxyp():
    pass


def cxywh_to_xyxyp():
    pass


def cxywhn_to_xyxyp():
    pass


def xyxyp_to_xyxyp(bounding_boxes):
    return bounding_boxes


def xywhp_to_xyxyp(bounding_boxes):
    return xywh_to_xyxy(bounding_boxes)


def cxywhp_to_xyxyp(bounding_boxes):
    return cxywh_to_xyxy(bounding_boxes)
