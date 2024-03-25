import cv2
import numpy as np


def create_fill_mask(image, coords):
    fill_mask = np.zeros(image.shape[:2], dtype=np.uint8)
    coords = coords.astype(int)
    cv2.fillPoly(fill_mask, [coords], 1)
    return fill_mask


def create_convex_mask(image, coords):
    convex_mask = np.zeros(image.shape[:2], dtype=np.uint8)
    hull = cv2.convexHull(coords.astype(int))
    cv2.fillConvexPoly(convex_mask, hull, 1)
    return convex_mask


def create_mask_from_bbox(image, bbox):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    x1, y1, x2, y2 = map(int, bbox)
    mask[y1:y2, x1:x2] = 1
    return mask
