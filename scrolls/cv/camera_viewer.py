import cv2


def camera_viewer(
    video_capture_input,
    windows_name='main',
    wait_key_delay=1,
):

    cap = cv2.VideoCapture(video_capture_input)  # rtsp://login:pass@ip

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(windows_name, frame)

        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camera_viewer(0)
