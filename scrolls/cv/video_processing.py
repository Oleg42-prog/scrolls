import os
import cv2


def first_frame(file_path):
    cap = cv2.VideoCapture(file_path)
    ret, frame = cap.read()
    cap.release()
    return ret, frame


def frames_reader(video_file_path):
    cap = cv2.VideoCapture(video_file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        yield frame


def frames_writer(folder, frames_generator):
    for frame_number, frame in enumerate(frames_generator):
        file_path = os.path.join(folder, f'{frame_number:04d}.png')
        cv2.imwrite(file_path, frame)
