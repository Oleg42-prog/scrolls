import cv2
from scrolls.cv.trackbars import UniformTrackbars
from scrolls.cv.filter_viewer import filter_image_viewer
from scrolls.geometry.projective import make_projective_transform


def projective_filter(image):
    return make_projective_transform(image, rotations.rx, rotations.ry, rotations.rz)


_image = cv2.imread('images/lena.png')
rotations = UniformTrackbars('Projective Filter', ['rx', 'ry', 'rz'], max_value=360)
filter_image_viewer(_image, projective_filter, 'Projective Filter')
