import cv2
import numpy as np
from scrolls.lists.matrix import matrix_map, flatten, np_matrix_stack
from scrolls.lists.func import conditional_return, all_equal


def camera_viewer(
    video_capture_input,
    window_name='main',
    wait_key_delay=1
):

    cap = cv2.VideoCapture(video_capture_input)  # rtsp://login:pass@ip

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(window_name, frame)

        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def multi_camera_viewer(
    matrix_of_video_capture_inputs,
    window_name='main',
    wait_key_delay=1,
    frame_filter=lambda x: x
):

    caps_matrix = matrix_map(cv2.VideoCapture, matrix_of_video_capture_inputs)

    widths = flatten(matrix_map(lambda cap: cap.get(cv2.CAP_PROP_FRAME_WIDTH), caps_matrix))
    heights = flatten(matrix_map(lambda cap: cap.get(cv2.CAP_PROP_FRAME_HEIGHT), caps_matrix))

    if not (all_equal(widths) and all_equal(heights)):
        raise ValueError('All video capture inputs must have the same resolution')

    width = int(widths[0])
    height = int(heights[0])

    black_screen = np.zeros((height, width, 3), np.uint8)

    while True:
        matrix_map(lambda cap: cap.grab(), caps_matrix)
        frames_matrix = matrix_map(lambda cap: conditional_return(*cap.retrieve(), black_screen), caps_matrix)
        frames_matrix = matrix_map(frame_filter, frames_matrix)

        union_frame = np_matrix_stack(frames_matrix)

        cv2.imshow(window_name, union_frame)
        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    for cap in flatten(caps_matrix):
        cap.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    camera_viewer(0)
