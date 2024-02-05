import cv2


def compress_twice(img):
    h, w, _ = img.shape
    return cv2.resize(img, (w // 2, h // 2))


def first_frame(file_path):
    cap = cv2.VideoCapture(file_path)
    ret, frame = cap.read()
    cap.release()
    return ret, frame


def binary_mask(image):
    _image = image.copy().astype('uint8')
    _image[_image > 0] = 1
    _image[_image <= 0] = 0
    return _image.astype('uint8')


def binary_mask_255(image):
    return binary_mask(image) * 255


def crop(img, x, y, width, height):
    return img[y:y+height, x:x+width].copy()
