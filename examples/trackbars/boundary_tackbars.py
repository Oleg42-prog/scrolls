import cv2
import numpy as np
from scrolls.cv.filter_viewer import filter_image_viewer
from scrolls.cv.trackbars import BoundaryTrackbars


def image_filter(image):

    image = image.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    color = (255, 255, 255)
    thickness = 2

    text = f'{trackbar.lower} / {trackbar.upper}'

    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_width, text_height = text_size
    x = (image.shape[1] - text_width) // 2
    y = (image.shape[0] + text_height) // 2

    return cv2.putText(image, text, (x, y), font, font_scale, color, thickness)


empty_image = np.zeros((800, 600, 3), np.uint8)
trackbar = BoundaryTrackbars('main')
filter_image_viewer(empty_image, image_filter)
