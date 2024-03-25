import cv2
import numpy as np


def to_radians(*degrees):
    np_degrees = np.array(degrees)
    return np_degrees * (np.pi / 180)


def rodrigues_degree(degree_x, degree_y, degree_z):
    rot_vec = to_radians(degree_x, degree_y, degree_z)
    rot_mat, _ = cv2.Rodrigues(rot_vec)
    return rot_mat
