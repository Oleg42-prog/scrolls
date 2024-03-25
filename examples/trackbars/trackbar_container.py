import cv2
import numpy as np
from scrolls.cv.filter_viewer import filter_video_viewer
from scrolls.cv.trackbars import TrackbarContainer, TrackbarDescription


def image_translation(img, x, y):
    rows, cols, _ = img.shape
    matrix = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])
    return cv2.warpAffine(img, matrix, (cols, rows))


def image_filter(img):
    return image_translation(img, trackbar.x, trackbar.y)


trackbar = TrackbarContainer('main', [
    TrackbarDescription('x', 50, 150),
    TrackbarDescription('y', 90, 300)
])
filter_video_viewer(0, image_filter)
