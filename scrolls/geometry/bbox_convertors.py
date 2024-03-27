def box_xyxy_to_xywh(bounding_box):
    bounding_boxes = bounding_box.reshape(1, -1)
    return boxes_xyxy_to_xywh(bounding_boxes)


def boxes_xyxy_to_xywh(bounding_boxes):
    pass


def boxes_xyxy_to_xyxyn(bounding_boxes, image_size):
    pass
