import cv2
import numpy as np
from scrolls.geometry.angles import rodrigues_degree


def camera_matrix_from_image(image):
    return np.array([
        [image.shape[0], 0, image.shape[1] / 2],
        [0, image.shape[0], image.shape[0] / 2],
        [0, 0, 1]
    ])


def create_projective_transform(image, degree_x, degree_y, degree_z):

    rot_mat = rodrigues_degree(degree_x, degree_y, degree_z)
    rot_mat[0, 2] = 0
    rot_mat[1, 2] = 0
    rot_mat[2, 2] = 1

    translation = np.array([
        [1, 0, -image.shape[1] / 2],
        [0, 1, -image.shape[0] / 2],
        [0, 0, 1]
    ])

    trans = np.dot(rot_mat, translation)
    trans[2, 2] += image.shape[0]

    camera_mat = camera_matrix_from_image(image)
    transform = np.dot(camera_mat, trans)

    return transform


def apply_projective_transform(image, transform):
    return cv2.warpPerspective(image, transform, (image.shape[1], image.shape[0]))


def make_projective_transform(image, degree_x, degree_y, degree_z):
    transform = create_projective_transform(image, degree_x, degree_y, degree_z)
    return apply_projective_transform(image, transform)
