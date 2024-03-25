import cv2
import numpy as np
from scrolls.cv.trackbars import UniformTrackbars
from scrolls.cv.filter_viewer import filter_image_viewer
from scrolls.geometry.masks import create_fill_mask, create_convex_mask
from scrolls.geometry.bboxes import calculate_bbox_from_points, calculate_bbox_from_mask
from scrolls.geometry.projective import create_projective_transform, apply_projective_transform
from scrolls.geometry.draw import draw_bbox, highlight_mask_on_image, draw_convex_hull


def make_projective_fill_mask_filter(yolo_mask, rotations):

    mask = create_fill_mask(_image, yolo_mask)

    def projective_filter(image):

        transform = create_projective_transform(image, rotations.rx, rotations.ry, rotations.rz)

        transformed_image = apply_projective_transform(image, transform)
        transformed_mask = apply_projective_transform(mask, transform)
        bbox = calculate_bbox_from_mask(transformed_mask)

        transformed_image = draw_bbox(transformed_image, bbox)
        transformed_image = highlight_mask_on_image(transformed_image, transformed_mask)

        return transformed_image

    return projective_filter


def make_projective_convex_mask_filter(yolo_mask, rotations):

    convex_mask = create_convex_mask(_image, yolo_mask)
    yolo_mask_coords = yolo_mask.reshape(-1, 1, 2)
    convex_hull_coords = cv2.convexHull(yolo_mask_coords)

    def projective_filter(image):

        transform = create_projective_transform(image, rotations.rx, rotations.ry, rotations.rz)

        transformed_convex_mask = apply_projective_transform(convex_mask, transform)
        transformed_image = apply_projective_transform(image, transform)
        transformed_convex_hull_coords = cv2.perspectiveTransform(convex_hull_coords, transform)
        transformed_convex_hull_coords = transformed_convex_hull_coords.astype(int)

        convex_hull_points = transformed_convex_hull_coords.reshape(-1, 2)
        bbox = calculate_bbox_from_points(convex_hull_points)

        transformed_image = draw_bbox(transformed_image, bbox)
        transformed_image = highlight_mask_on_image(transformed_image, transformed_convex_mask)
        transformed_image = draw_convex_hull(transformed_image, transformed_convex_hull_coords, draw_points=True)

        return transformed_image

    return projective_filter


def make_double_filter(yolo_mask, rotations):
    fill_mask_filter = make_projective_fill_mask_filter(yolo_mask, rotations)
    convex_mask_filter = make_projective_convex_mask_filter(yolo_mask, rotations)

    def double_filter(image):
        return np.hstack([fill_mask_filter(image), convex_mask_filter(image)])

    return double_filter


INPUT_FILE_TITLE = 'oleg'  # lena, oleg
_image = cv2.imread(f'images/{INPUT_FILE_TITLE}.png')
_mask = np.load(f'images/masks/{INPUT_FILE_TITLE}.npy')

rotations_trackbars = UniformTrackbars('Rotations', ['rx', 'ry', 'rz'], max_value=360)
main_filter = make_double_filter(_mask, rotations_trackbars)
filter_image_viewer(_image, main_filter, 'Projective')
