from scrolls.geometry.boxes.to_xywh import xyxy_to_xywh as boxes_xyxy_to_xywh


def box_xyxy_to_xywh(bounding_box):
    bounding_boxes = bounding_box.reshape(1, -1)
    return boxes_xyxy_to_xywh(bounding_boxes)
