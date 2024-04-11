from scrolls.geometry.boxes.convertors.synonyms.normalised import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import cxywhn_to_xyxyn, cxywhn_to_xywhn

from scrolls.geometry.boxes.convertors.synonyms.percentaged import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xywhp_to_xyxyp, xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import cxywhp_to_xyxyp, cxywhp_to_xywhp

__all__ = [
    'xyxyn_to_xywhn', 'xyxyn_to_cxywhn',
    'xywhn_to_xyxyn', 'xywhn_to_cxywhn',
    'cxywhn_to_xyxyn', 'cxywhn_to_xywhn',

    'xyxyp_to_xywhp', 'xyxyp_to_cxywhp',
    'xywhp_to_xyxyp', 'xywhp_to_cxywhp',
    'cxywhp_to_xyxyp', 'cxywhp_to_xywhp',
]
