import cv2


def draw_bbox(image, bbox):
    image = image.copy()
    x1, y1, x2, y2 = bbox
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return image


def draw_convex_hull(image, convex_hull, draw_points=False):
    image = image.copy()
    cv2.polylines(image, [convex_hull], True, (0, 255, 0), 2)

    if draw_points:
        for point in convex_hull:
            cv2.circle(image, tuple(point[0]), 5, (0, 0, 255), -1)
        cv2.polylines(image, [convex_hull], True, (255, 0, 0), 2)

    return image


def highlight_mask_on_image(image, mask, color=(0, 0, 255), alpha=0.5):
    image = image.copy()
    overlay = image.copy()
    overlay[mask == 1] = color
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
    return image
