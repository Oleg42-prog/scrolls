import cv2
import numpy as np


class HSVTrackbar:

    def __init__(self, window_name):
        self.colors = 'hsv'
        self.window_name = window_name

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        for color in self.colors:
            cv2.createTrackbar(f'lower {color}', window_name, 0, 255, lambda x: x)
            cv2.createTrackbar(f'upper {color}', window_name, 0, 255, lambda x: x)

    def get(self, bound, color):
        return cv2.getTrackbarPos(f'{bound} {color}', self.window_name)

    @property
    def lower(self):
        return np.array([self.get('lower', color) for color in self.colors])

    @property
    def upper(self):
        return np.array([self.get('upper', color) for color in self.colors])
