import cv2
from scrolls.cv.image_processing import compress_twice, image_in_range
from scrolls.cv.bounds_trackbar import BoundsTrackbar
from scrolls.cv.filter_viewer import filter_viewer


def image_filter(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = compress_twice(image)
    return image_in_range(image, trackbar.lower, trackbar.upper)


trackbar = BoundsTrackbar('main')
filter_viewer(0, image_filter)
