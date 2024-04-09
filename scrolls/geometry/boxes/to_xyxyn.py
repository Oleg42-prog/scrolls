from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy


def xyxy_to_xyxyn():
    pass


def xywh_to_xyxyn():
    pass


def xyxyn_to_xyxyn(bounding_boxes):
    return bounding_boxes


def xywhn_to_xyxyn(bounding_boxes):
    return xywh_to_xyxy(bounding_boxes)


def cxywh_to_xyxyn():
    pass


def cxywhn_to_xyxyn(bounding_boxes):
    return cxywh_to_xyxy(bounding_boxes)


def xyxyp_to_xyxyn(bounding_boxes):
    return bounding_boxes / 100


def xywhp_to_xyxyn():
    pass


def cxywhp_to_xyxyn():
    pass
