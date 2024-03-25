import numpy as np


def calculate_bbox_from_points(points):
    x_min, y_min = np.min(points, axis=0)
    x_max, y_max = np.max(points, axis=0)
    return [x_min, y_min, x_max, y_max]


def calculate_bbox_from_mask(mask):
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    y1, y2 = np.where(rows)[0][[0, -1]]
    x1, x2 = np.where(cols)[0][[0, -1]]
    return [x1, y1, x2, y2]


def yolo_to_xyxy(yolo_bbox):

    x_center, y_center, width, height = yolo_bbox

    x1 = int(x_center - (width / 2))
    y1 = int(y_center - (height / 2))
    x2 = int(x_center + (width / 2))
    y2 = int(y_center + (height / 2))

    return [x1, y1, x2, y2]
