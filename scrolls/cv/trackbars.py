import cv2
import numpy as np


class Trackbar:

    def __init__(self, window_name, trackbar_name, init_value=0, max_value=255):
        self.window_name = window_name
        self.trackbar_name = trackbar_name

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.createTrackbar(trackbar_name, window_name, init_value, max_value, lambda x: x)

    @property
    def value(self):
        return cv2.getTrackbarPos(self.trackbar_name, self.window_name)


class BoundaryTrackbars:

    def __init__(self, window_name, init_lower=0, init_upper=255, max_value=255, lower_name='lower', upper_name='upper'):
        self.lower_trackbar = Trackbar(window_name, lower_name, init_value=init_lower, max_value=max_value)
        self.upper_trackbar = Trackbar(window_name, upper_name, init_value=init_upper, max_value=max_value)

    @property
    def lower(self):
        return self.lower_trackbar.value

    @property
    def upper(self):
        return self.upper_trackbar.value


class ColorBoundaryTrackbars:

    def __init__(self, window_name, colors):
        self.window_name = window_name
        self.colors = colors

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        for color in colors:
            cv2.createTrackbar(f'lower {color}', window_name, 0, 255, lambda x: x)
            cv2.createTrackbar(f'upper {color}', window_name, 0, 255, lambda x: x)

    def get_lower(self, name):
        return cv2.getTrackbarPos(f'lower {name}', self.window_name)

    @property
    def lower(self):
        return np.array([self.get_lower(color) for color in self.colors])

    def get_upper(self, name):
        return cv2.getTrackbarPos(f'upper {name}', self.window_name)

    @property
    def upper(self):
        return np.array([self.get_upper(color) for color in self.colors])


class HSVTrackbar:

    def __init__(self, window_name):
        self.colors = 'hsv'
        self.window_name = window_name

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        for color in self.colors:
            cv2.createTrackbar(f'lower {color}', window_name, 0, 255, lambda x: x)
            cv2.createTrackbar(f'upper {color}', window_name, 255, 255, lambda x: x)

    def get(self, bound, color):
        return cv2.getTrackbarPos(f'{bound} {color}', self.window_name)

    @property
    def lower(self):
        return np.array([self.get('lower', color) for color in self.colors])

    @property
    def upper(self):
        return np.array([self.get('upper', color) for color in self.colors])
