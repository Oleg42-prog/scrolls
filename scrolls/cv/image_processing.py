import cv2
import numpy as np
from PIL import Image
from scrolls.geometry.linal import min_max_scaller


def compress_twice(img):
    h, w = img.shape[:2]
    return cv2.resize(img, (w // 2, h // 2))


def binary_mask(image):
    _image = image.copy().astype('uint8')
    _image[_image > 0] = 1
    _image[_image <= 0] = 0
    return _image.astype('uint8')


def binary_mask_255(image):
    return binary_mask(image) * 255


def padding(p, x, y, w, h):
    return x - p, y - p, w + p * 2, h + p * 2


def crop(image, x, y, w, h):
    return image[y:y+h, x:x+w].copy()


def image_in_range(img, lower, upper):
    mask = cv2.inRange(img, lower, upper)
    return cv2.bitwise_and(img, img, mask=mask)


def invert(image):
    return 255 - image


def to_image_255(image):
    normalized = min_max_scaller(image)
    return np.uint8(normalized * 255)


def triple_channel(img):
    return cv2.merge((img, img, img))


def everything_to_pil_image(input_data):

    if isinstance(input_data, str):
        return Image.open(input_data)

    if isinstance(input_data, np.ndarray):
        return Image.fromarray(input_data.astype('uint8'))

    if isinstance(input_data, Image.Image):
        return input_data

    raise ValueError("Input type not recognized. It should be either a file path, a numpy array, or a PIL Image.")
