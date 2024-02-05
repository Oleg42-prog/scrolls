import cv2


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


def crop(img, x, y, width, height):
    return img[y:y+height, x:x+width].copy()


def image_in_range(img, lower, upper):
    mask = cv2.inRange(img, lower, upper)
    return cv2.bitwise_and(img, img, mask=mask)


def invert(image):
    return 255 - image
