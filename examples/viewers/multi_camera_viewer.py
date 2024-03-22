from scrolls.lists.matrix import matrix_map
from scrolls.cv.camera_viewer import multi_camera_viewer
from scrolls.cv.filters import resizer

cameras_names_matrix = [
    ['/stream', '/stream'],
    ['/stream', '/stream'],
]

RTSP_URL = 'rtsp://rtsp-test-server.viomic.com:554'
matrix_of_video_capture_inputs = matrix_map(lambda name: RTSP_URL + name, cameras_names_matrix)
multi_camera_viewer(matrix_of_video_capture_inputs, frame_filter=resizer(1920 // 2, 1080 // 2))
