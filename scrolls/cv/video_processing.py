import cv2


def first_frame(file_path):
    cap = cv2.VideoCapture(file_path)
    ret, frame = cap.read()
    cap.release()
    return ret, frame
