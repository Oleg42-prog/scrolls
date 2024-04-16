from dataclasses import dataclass
import numpy as np


@dataclass
class BoxNormalisedRepresentations:
    xyxyn: np.array
    xywhn: np.array
    cxywhn: np.array
    original_width: int
    original_height: int


EMPTY = BoxNormalisedRepresentations(
    xyxyn=np.array([]),
    xywhn=np.array([]),
    cxywhn=np.array([]),
    original_width=0,
    original_height=0
)

NORMALISED_LEFT_BIRD = BoxNormalisedRepresentations(
    xyxyn=np.array([0.151, 0.11272727272727273, 0.386, 0.9581818181818181]),
    xywhn=np.array([0.151, 0.11272727272727273, 0.235, 0.8454545454545455]),
    cxywhn=np.array([0.2685, 0.5354545454545454, 0.235, 0.8454545454545455]),
    original_width=1000,
    original_height=550
)


NORMALISED_RIGHT_BIRD = BoxNormalisedRepresentations(
    xyxyn=np.array([0.43, 0.16, 0.962, 0.9145454545454546]),
    xywhn=np.array([0.43, 0.16, 0.532, 0.7545454545454545]),
    cxywhn=np.array([0.696, 0.5372727272727272, 0.532, 0.7545454545454545]),
    original_width=1000,
    original_height=550
)

NORMALISED_UNION_BIRDS = BoxNormalisedRepresentations(
    xyxyn=np.vstack([NORMALISED_LEFT_BIRD.xyxyn, NORMALISED_RIGHT_BIRD.xyxyn]),
    xywhn=np.vstack([NORMALISED_LEFT_BIRD.xywhn, NORMALISED_RIGHT_BIRD.xywhn]),
    cxywhn=np.vstack([NORMALISED_LEFT_BIRD.cxywhn, NORMALISED_RIGHT_BIRD.cxywhn]),
    original_width=1000,
    original_height=550
)
