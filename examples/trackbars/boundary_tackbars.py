import cv2
import numpy as np
from scrolls.cv.filter_viewer import filter_image_viewer
from scrolls.cv.trackbars import BoundaryTrackbars


def calculate_text_center_position(image, text, font, font_scale, thickness):
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_width, text_height = text_size
    x = (image.shape[1] - text_width) // 2
    y = (image.shape[0] + text_height) // 2
    return x, y


def draw_center_text(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    color = (255, 255, 255)
    thickness = 3
    x, y = calculate_text_center_position(image, text, font, font_scale, thickness)
    return cv2.putText(image, text, (x, y), font, font_scale, color, thickness)


def image_filter(image):
    image = image.copy()
    text = f'{trackbar.lower} / {trackbar.upper}'
    return draw_center_text(image, text)


empty_image = np.zeros((800, 600, 3), np.uint8)
trackbar = BoundaryTrackbars('main')
filter_image_viewer(empty_image, image_filter)
