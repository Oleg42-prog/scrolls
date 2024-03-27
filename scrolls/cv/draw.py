import cv2


def draw_xywh_bbox(img, bbox, color=(255, 0, 0)):
    x, y, w, h = map(int, bbox)
    return cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
