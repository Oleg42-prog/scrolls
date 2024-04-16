from dataclasses import dataclass
import numpy as np


@dataclass
class BoxPercentagedRepresentations:
    xyxyp: np.array
    xywhp: np.array
    cxywhp: np.array
    original_width: int
    original_height: int


EMPTY = BoxPercentagedRepresentations(
    xyxyp=np.array([]),
    xywhp=np.array([]),
    cxywhp=np.array([]),
    original_width=0,
    original_height=0
)

PERCENTAGED_LEFT_BIRD = BoxPercentagedRepresentations(
    xyxyp=np.array([(15.1, 11.272727272727273, 38.6, 95.81818181818181)]),
    xywhp=np.array([(15.1, 11.272727272727273, 23.5, 84.54545454545455)]),
    cxywhp=np.array([(26.85, 53.54545454545454, 23.5, 84.54545454545455)]),
    original_width=1000,
    original_height=550
)


PERCENTAGED_RIGHT_BIRD = BoxPercentagedRepresentations(
    xyxyp=np.array([43.0, 16.0, 96.2, 91.45454545454545]),
    xywhp=np.array([43.0, 16.0, 53.2, 75.45454545454545]),
    cxywhp=np.array([69.6, 53.72727272727273, 53.2, 75.45454545454545]),
    original_width=1000,
    original_height=550
)

PERCENTAGED_UNION_BIRDS = BoxPercentagedRepresentations(
    xyxyp=np.vstack([PERCENTAGED_LEFT_BIRD.xyxyp, PERCENTAGED_RIGHT_BIRD.xyxyp]),
    xywhp=np.vstack([PERCENTAGED_LEFT_BIRD.xywhp, PERCENTAGED_RIGHT_BIRD.xywhp]),
    cxywhp=np.vstack([PERCENTAGED_LEFT_BIRD.cxywhp, PERCENTAGED_RIGHT_BIRD.cxywhp]),
    original_width=1000,
    original_height=550
)
