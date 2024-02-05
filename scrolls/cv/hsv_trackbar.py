import cv2


class HSVTrackbar:

    def __init__(self, window_name):
        self.window_name = window_name
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        cv2.createTrackbar('lower h', window_name, 0, 255, lambda x: x)
        cv2.createTrackbar('lower s', window_name, 0, 255, lambda x: x)
        cv2.createTrackbar('lower v', window_name, 0, 255, lambda x: x)

        cv2.createTrackbar('upper h', window_name, 0, 255, lambda x: x)
        cv2.createTrackbar('upper s', window_name, 0, 255, lambda x: x)
        cv2.createTrackbar('upper v', window_name, 0, 255, lambda x: x)

    @property
    def lower_h(self):
        return cv2.getTrackbarPos('lower h', self.window_name)

    @property
    def lower_s(self):
        return cv2.getTrackbarPos('lower s', self.window_name)

    @property
    def lower_v(self):
        return cv2.getTrackbarPos('lower v', self.window_name)

    @property
    def lower(self):
        return [self.lower_h, self.lower_s, self.lower_v]

    @property
    def upper_h(self):
        return cv2.getTrackbarPos('upper h', self.window_name)

    @property
    def upper_s(self):
        return cv2.getTrackbarPos('upper s', self.window_name)

    @property
    def upper_v(self):
        return cv2.getTrackbarPos('upper v', self.window_name)

    @property
    def upper(self):
        return [self.upper_h, self.upper_s, self.upper_v]
