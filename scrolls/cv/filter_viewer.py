import cv2


def filter_video_viewer(video_capture_input, image_filter, windows_name='main', wait_key_delay=1):

    cap = cv2.VideoCapture(video_capture_input)

    while True:
        ret, image = cap.read()

        if ret is not True:
            break

        cv2.imshow(windows_name, image_filter(image))

        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def filter_image_viewer(image, image_filter, windows_name='main', wait_key_delay=1):

    while True:

        cv2.imshow(windows_name, image_filter(image))

        if cv2.waitKey(wait_key_delay) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
