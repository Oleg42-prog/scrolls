import cv2


def filter_video_viewer(
    video_capture_input,
    image_filter,
    windows_name='main',
    wait_key_delay=1,
    loop=False
):

    cap = cv2.VideoCapture(video_capture_input)
    frames_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_number = 0

    while True:
        ret, image = cap.read()

        if loop and frame_number >= frames_count:
            frame_number = 0
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        if ret is not True:
            break

        cv2.imshow(windows_name, image_filter(image))
        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()


def filter_image_viewer(image, image_filter, windows_name='main', wait_key_delay=1):

    while True:

        cv2.imshow(windows_name, image_filter(image))

        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
