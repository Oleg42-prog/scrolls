import cv2
from scrolls.cv.image_processing import compress_twice, image_in_range
from scrolls.cv.filter_viewer import filter_video_viewer
from scrolls.cv.hsv_trackbar import HSVTrackbar


def image_filter(img):
    img = compress_twice(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    out_img = image_in_range(img, trackbar.lower, trackbar.upper)
    out_img = cv2.cvtColor(out_img, cv2.COLOR_HSV2BGR)
    return out_img


trackbar = HSVTrackbar('main')
filter_video_viewer(0, image_filter)
