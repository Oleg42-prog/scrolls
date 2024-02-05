import cv2


def compress_twice(img):
    h, w, _ = img.shape
    return cv2.resize(img, (w // 2, h // 2))
