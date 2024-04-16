from dataclasses import dataclass
import numpy as np


@dataclass
class BoxRepresentations:
    xyxy: np.array
    xywh: np.array
    cxywh: np.array


LEFT_BIRD = BoxRepresentations(
    xyxy=np.array([151, 62, 386, 527]),
    xywh=np.array([151, 62, 235, 465]),
    cxywh=np.array([268.5, 294.5, 235, 465])
)

RIGHT_BIRD = BoxRepresentations(
    xyxy=np.array([430, 88, 962, 503]),
    xywh=np.array([430, 88, 532, 415]),
    cxywh=np.array([696, 295.5, 532, 415])
)

UNION_BIRDS = BoxRepresentations(
    xyxy=np.vstack([LEFT_BIRD.xyxy, RIGHT_BIRD.xyxy]),
    xywh=np.vstack([LEFT_BIRD.xywh, RIGHT_BIRD.xywh]),
    cxywh=np.vstack([LEFT_BIRD.cxywh, RIGHT_BIRD.cxywh])
)
