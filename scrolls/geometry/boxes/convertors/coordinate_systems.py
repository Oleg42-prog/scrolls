from scrolls.geometry.boxes.transforms import normalize_bounding_boxes, rescale_bounding_boxes


def original_to_normalized(xywh, original_size):
    return normalize_bounding_boxes(xywh, original_size)


def normalized_to_original(boxes, original_size):
    return rescale_bounding_boxes(boxes, original_size)


def normalized_to_percentaged(boxes):
    return boxes * 100


def percentaged_to_normalized(boxes):
    return boxes / 100


def original_to_percentaged(boxes, original_size):
    normalized = original_to_normalized(boxes, original_size)
    return normalized_to_percentaged(normalized)


def percentaged_to_original(boxes, original_size):
    normalized = percentaged_to_normalized(boxes)
    return normalized_to_original(normalized, original_size)
