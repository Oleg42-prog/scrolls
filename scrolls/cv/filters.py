import cv2


def resizer(new_width, new_height, interpolation=cv2.INTER_AREA):
    return lambda img: cv2.resize(img, (new_width, new_height), interpolation=interpolation)
