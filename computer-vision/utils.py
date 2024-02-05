import cv2


def compress_twice(img):
    h, w, _ = img.shape
    return cv2.resize(img, (w // 2, h // 2))


def first_frame(file_path):
    cap = cv2.VideoCapture(file_path)
    ret, frame = cap.read()
    cap.release()
    return ret, frame
