from scrolls.geometry.boxes.transforms import rescale_bounding_boxes
from scrolls.geometry.boxes.to_xywh import xywhp_to_xywh
from scrolls.geometry.boxes.to_cxywh import cxywhp_to_cxywh

from scrolls.geometry.boxes.convertors.identity import xyxy_to_xyxy
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy
from scrolls.geometry.boxes.convertors.from_normalised import xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import xywhn_to_xyxy
from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import cxywhn_to_xyxy
from scrolls.geometry.boxes.convertors.from_percentaged import xyxyp_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import xywhp_to_xyxy
from scrolls.geometry.boxes.convertors.complicated import cxywhp_to_xyxy
