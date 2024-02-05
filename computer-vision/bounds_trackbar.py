import cv2


class BoundsTrackbar:

    def __init__(self, window_name, init_lower=0, init_upper=255, max_value=255):
        self.window_name = window_name
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        cv2.createTrackbar('lower', self.window_name, init_lower, max_value, lambda x: x)
        cv2.createTrackbar('upper', self.window_name, init_upper, max_value, lambda x: x)

    @property
    def lower(self):
        return cv2.getTrackbarPos('lower', self.window_name)

    @property
    def upper(self):
        return cv2.getTrackbarPos('upper', self.window_name)
