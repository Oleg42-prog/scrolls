from dataclasses import dataclass, asdict

import cv2
import numpy as np


@dataclass
class TrackbarDescription:
    trackbar_name: str
    init_value: int = 0
    max_value: int = 100


class Trackbar:

    def __init__(self, window_name, trackbar_name, init_value=0, max_value=100):
        self.window_name = window_name
        self.trackbar_name = trackbar_name

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.createTrackbar(trackbar_name, window_name, init_value, max_value, lambda x: x)

    @property
    def value(self):
        return cv2.getTrackbarPos(self.trackbar_name, self.window_name)

    @staticmethod
    def from_description(window_name, description):
        return Trackbar(window_name, **asdict(description))


class TrackbarContainer:

    def __init__(self, window_name, descriptions):
        self._container = {}
        self.window_name = window_name

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        for descr in descriptions:
            self._container[descr.trackbar_name] = Trackbar.from_description(window_name, descr)

    def __getitem__(self, trackbar_name):
        return self.value(trackbar_name)

    def __getattr__(self, trackbar_name):
        if trackbar_name in self._container:
            return self.value(trackbar_name)
        raise AttributeError(f'No such trackbar: {trackbar_name}')

    def value(self, trackbar_name):
        return self._container[trackbar_name].value


class UniformTrackbars(TrackbarContainer):

    def __init__(self, window_name, trackbars_names, init_value=0, max_value=100):
        descriptions = []
        for trackbar_name in trackbars_names:
            uniform_description = TrackbarDescription(trackbar_name, init_value, max_value)
            descriptions.append(uniform_description)
        super().__init__(window_name, descriptions)


class BoundaryTrackbars:

    def __init__(
        self,
        window_name,
        lower_description=TrackbarDescription('lower', 0, 100),
        upper_description=TrackbarDescription('upper', 100, 100)
    ):
        self.lower_trackbar = Trackbar.from_description(window_name, lower_description)
        self.upper_trackbar = Trackbar.from_description(window_name, upper_description)

    @property
    def lower(self):
        return self.lower_trackbar.value

    @property
    def upper(self):
        return self.upper_trackbar.value


class GrayscaleTrackbars(BoundaryTrackbars):

    def __init__(self, window_name):
        super().__init__(window_name, TrackbarDescription('lower', 0, 255), TrackbarDescription('upper', 255, 255))


class ColorTrackbars:

    def __init__(self, window_name, colors):
        self.window_name = window_name
        self.colors = colors

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        for color in self.colors:
            cv2.createTrackbar(f'lower {color}', window_name, 0, 255, lambda x: x)
            cv2.createTrackbar(f'upper {color}', window_name, 255, 255, lambda x: x)

    def get(self, bound, color):
        return cv2.getTrackbarPos(f'{bound} {color}', self.window_name)

    def get_lower(self, color):
        return self.get('lower', color)

    def get_upper(self, color):
        return self.get('upper', color)

    @property
    def lowers(self):
        return np.array([self.get_lower(color) for color in self.colors])

    @property
    def uppers(self):
        return np.array([self.get_upper(color) for color in self.colors])

    def get_bounds(self, color):
        return np.array([self.get('lower', color), self.get('upper', color)])

    def __getattr__(self, color):
        if color in self.colors:
            return self.get_bounds(color)
        raise AttributeError(f'No such color: {color}')


class HSVTrackbars(ColorTrackbars):

    def __init__(self, window_name):
        super().__init__(window_name, 'hsv')


class RGBTrackbars(ColorTrackbars):

    def __init__(self, window_name):
        super().__init__(window_name, 'rgb')
