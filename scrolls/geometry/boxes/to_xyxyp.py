from scrolls.geometry.boxes.to_xyxy import xywh_to_xyxy, cxywh_to_xyxy
from scrolls.geometry.boxes.to_xyxyn import xyxy_to_xyxyn, xywh_to_xyxyn, xywhn_to_xyxyn


def xyxy_to_xyxyp(bounding_boxes, image_size):
    return xyxy_to_xyxyn(bounding_boxes, image_size) * 100


def xywh_to_xyxyp(bounding_boxes, image_size):
    return xywh_to_xyxyn(bounding_boxes, image_size) * 100


def xyxyn_to_xyxyp(bounding_boxes):
    return bounding_boxes * 100


def xywhn_to_xyxyp(bounding_boxes):
    return xywhn_to_xyxyn(bounding_boxes) * 100


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
