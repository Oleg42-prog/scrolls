from scrolls.geometry.boxes.convertors.identity import xyxyp_to_xyxyp
from scrolls.geometry.boxes.convertors.identity import xyxyn_to_xyxyn
from scrolls.geometry.boxes.convertors.identity import xyxy_to_xyxy
from scrolls.geometry.boxes.convertors.identity import xywhp_to_xywhp
from scrolls.geometry.boxes.convertors.identity import xywhn_to_xywhn
from scrolls.geometry.boxes.convertors.identity import xywh_to_xywh
from scrolls.geometry.boxes.convertors.identity import cxywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.identity import cxywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.identity import cxywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations import xyxyp_to_xywhp
from scrolls.geometry.boxes.convertors.representations import xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations import xyxyn_to_xywhn
from scrolls.geometry.boxes.convertors.representations import xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xyxy_to_xywh
from scrolls.geometry.boxes.convertors.representations import xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations import xywhp_to_xyxyp
from scrolls.geometry.boxes.convertors.representations import xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations import xywhn_to_xyxyn
from scrolls.geometry.boxes.convertors.representations import xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations import xywh_to_xyxy
from scrolls.geometry.boxes.convertors.representations import xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations import cxywhp_to_xyxyp
from scrolls.geometry.boxes.convertors.representations import cxywhp_to_xywhp
from scrolls.geometry.boxes.convertors.representations import cxywhn_to_xyxyn
from scrolls.geometry.boxes.convertors.representations import cxywhn_to_xywhn
from scrolls.geometry.boxes.convertors.representations import cxywh_to_xyxy
from scrolls.geometry.boxes.convertors.representations import cxywh_to_xywh
from scrolls.geometry.boxes.convertors.simple import xyxyp_to_xyxyn
from scrolls.geometry.boxes.convertors.simple import xyxyp_to_xyxy
from scrolls.geometry.boxes.convertors.simple import xyxyn_to_xyxyp
from scrolls.geometry.boxes.convertors.simple import xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyp
from scrolls.geometry.boxes.convertors.simple import xyxy_to_xyxyn
from scrolls.geometry.boxes.convertors.simple import xywhp_to_xywhn
from scrolls.geometry.boxes.convertors.simple import xywhp_to_xywh
from scrolls.geometry.boxes.convertors.simple import xywhn_to_xywhp
from scrolls.geometry.boxes.convertors.simple import xywhn_to_xywh
from scrolls.geometry.boxes.convertors.simple import xywh_to_xywhp
from scrolls.geometry.boxes.convertors.simple import xywh_to_xywhn
from scrolls.geometry.boxes.convertors.simple import cxywhp_to_cxywhn
from scrolls.geometry.boxes.convertors.simple import cxywhp_to_cxywh
from scrolls.geometry.boxes.convertors.simple import cxywhn_to_cxywhp
from scrolls.geometry.boxes.convertors.simple import cxywhn_to_cxywh
from scrolls.geometry.boxes.convertors.simple import cxywh_to_cxywhp
from scrolls.geometry.boxes.convertors.simple import cxywh_to_cxywhn
from scrolls.geometry.boxes.convertors.complicated import xyxyp_to_xywhn
from scrolls.geometry.boxes.convertors.complicated import xyxyp_to_xywh
from scrolls.geometry.boxes.convertors.complicated import xyxyp_to_cxywhn
from scrolls.geometry.boxes.convertors.complicated import xyxyp_to_cxywh
from scrolls.geometry.boxes.convertors.complicated import xyxyn_to_xywhp
from scrolls.geometry.boxes.convertors.complicated import xyxyn_to_xywh
from scrolls.geometry.boxes.convertors.complicated import xyxyn_to_cxywhp
from scrolls.geometry.boxes.convertors.complicated import xyxyn_to_cxywh
from scrolls.geometry.boxes.convertors.complicated import xyxy_to_xywhp
from scrolls.geometry.boxes.convertors.complicated import xyxy_to_xywhn
from scrolls.geometry.boxes.convertors.complicated import xyxy_to_cxywhp
from scrolls.geometry.boxes.convertors.complicated import xyxy_to_cxywhn
from scrolls.geometry.boxes.convertors.complicated import xywhp_to_xyxyn
from scrolls.geometry.boxes.convertors.complicated import xywhp_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import xywhp_to_cxywhn
from scrolls.geometry.boxes.convertors.complicated import xywhp_to_cxywh
from scrolls.geometry.boxes.convertors.complicated import xywhn_to_xyxyp
from scrolls.geometry.boxes.convertors.complicated import xywhn_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import xywhn_to_cxywhp
from scrolls.geometry.boxes.convertors.complicated import xywhn_to_cxywh
from scrolls.geometry.boxes.convertors.complicated import xywh_to_xyxyp
from scrolls.geometry.boxes.convertors.complicated import xywh_to_xyxyn
from scrolls.geometry.boxes.convertors.complicated import xywh_to_cxywhp
from scrolls.geometry.boxes.convertors.complicated import xywh_to_cxywhn
from scrolls.geometry.boxes.convertors.complicated import cxywhp_to_xyxyn
from scrolls.geometry.boxes.convertors.complicated import cxywhp_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import cxywhp_to_xywhn
from scrolls.geometry.boxes.convertors.complicated import cxywhp_to_xywh
from scrolls.geometry.boxes.convertors.complicated import cxywhn_to_xyxyp
from scrolls.geometry.boxes.convertors.complicated import cxywhn_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import cxywhn_to_xywhp
from scrolls.geometry.boxes.convertors.complicated import cxywhn_to_xywh
from scrolls.geometry.boxes.convertors.complicated import cxywh_to_xyxyp
from scrolls.geometry.boxes.convertors.complicated import cxywh_to_xyxyn
from scrolls.geometry.boxes.convertors.complicated import cxywh_to_xywhp
from scrolls.geometry.boxes.convertors.complicated import cxywh_to_xywhn


__all__ = [
    'xyxy_to_xyxy',
    'xyxy_to_xywh',
    'xyxy_to_cxywh',
    'xywh_to_xyxy',
    'xywh_to_xywh',
    'xywh_to_cxywh',
    'cxywh_to_xyxy',
    'cxywh_to_xywh',
    'cxywh_to_cxywh',
    'xyxy_to_xyxyn',
    'xyxy_to_xywhn',
    'xyxy_to_cxywhn',
    'xywh_to_xyxyn',
    'xywh_to_xywhn',
    'xywh_to_cxywhn',
    'cxywh_to_xyxyn',
    'cxywh_to_xywhn',
    'cxywh_to_cxywhn',
    'xyxy_to_xyxyp',
    'xyxy_to_xywhp',
    'xyxy_to_cxywhp',
    'xywh_to_xyxyp',
    'xywh_to_xywhp',
    'xywh_to_cxywhp',
    'cxywh_to_xyxyp',
    'cxywh_to_xywhp',
    'cxywh_to_cxywhp',
    'xyxyn_to_xyxy',
    'xyxyn_to_xywh',
    'xyxyn_to_cxywh',
    'xywhn_to_xyxy',
    'xywhn_to_xywh',
    'xywhn_to_cxywh',
    'cxywhn_to_xyxy',
    'cxywhn_to_xywh',
    'cxywhn_to_cxywh',
    'xyxyn_to_xyxyn',
    'xyxyn_to_xywhn',
    'xyxyn_to_cxywhn',
    'xywhn_to_xyxyn',
    'xywhn_to_xywhn',
    'xywhn_to_cxywhn',
    'cxywhn_to_xyxyn',
    'cxywhn_to_xywhn',
    'cxywhn_to_cxywhn',
    'xyxyn_to_xyxyp',
    'xyxyn_to_xywhp',
    'xyxyn_to_cxywhp',
    'xywhn_to_xyxyp',
    'xywhn_to_xywhp',
    'xywhn_to_cxywhp',
    'cxywhn_to_xyxyp',
    'cxywhn_to_xywhp',
    'cxywhn_to_cxywhp',
    'xyxyp_to_xyxy',
    'xyxyp_to_xywh',
    'xyxyp_to_cxywh',
    'xywhp_to_xyxy',
    'xywhp_to_xywh',
    'xywhp_to_cxywh',
    'cxywhp_to_xyxy',
    'cxywhp_to_xywh',
    'cxywhp_to_cxywh',
    'xyxyp_to_xyxyn',
    'xyxyp_to_xywhn',
    'xyxyp_to_cxywhn',
    'xywhp_to_xyxyn',
    'xywhp_to_xywhn',
    'xywhp_to_cxywhn',
    'cxywhp_to_xyxyn',
    'cxywhp_to_xywhn',
    'cxywhp_to_cxywhn',
    'xyxyp_to_xyxyp',
    'xyxyp_to_xywhp',
    'xyxyp_to_cxywhp',
    'xywhp_to_xyxyp',
    'xywhp_to_xywhp',
    'xywhp_to_cxywhp',
    'cxywhp_to_xyxyp',
    'cxywhp_to_xywhp',
    'cxywhp_to_cxywhp',
]
