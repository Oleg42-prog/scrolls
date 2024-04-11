from scrolls.geometry.boxes.transforms import normalize_bounding_boxes, rescale_bounding_boxes
from scrolls.geometry.boxes.convertors.from_normalised import cxywhn_to_cxywh, xywhn_to_xywh, xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.from_percentaged import cxywhp_to_cxywh, xywhp_to_xywh, xyxyp_to_xyxy
from scrolls.geometry.boxes.convertors.to_normalised import xyxy_to_xyxyn, xywh_to_xywhn, cxywh_to_cxywhn
from scrolls.geometry.boxes.convertors.to_normalised import xyxyp_to_xyxyn, xywhp_to_xywhn, cxywhp_to_cxywhn
from scrolls.geometry.boxes.convertors.to_percentaged import xyxy_to_xyxyp, xywh_to_xywhp, cxywh_to_cxywhp
from scrolls.geometry.boxes.convertors.to_percentaged import xyxyn_to_xyxyp, xywhn_to_xywhp, cxywhn_to_cxywhp
from scrolls.geometry.boxes.convertors.representation import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representation import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representation import cxywh_to_xyxy, cxywh_to_xywh
from scrolls.geometry.boxes.convertors.synonyms.normalised import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.synonyms.normalised import cxywhn_to_xyxyn, cxywhn_to_xywhn
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import xywhp_to_xyxyp, xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.synonyms.percentaged import cxywhp_to_xyxyp, cxywhp_to_xywhp


def xyxyn_to_cxywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhn_to_cxywh(xywhn, image_size):
    xywh = xywhn_to_xywh(xywhn, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def xyxyp_to_cxywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    cxywh = xyxy_to_cxywh(xyxy)
    return cxywh


def xywhp_to_cxywh(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    cxywh = xywh_to_cxywh(xywh)
    return cxywh


def xyxy_to_cxywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywh_to_cxywhn(xywh, image_size):
    xywhn = xywh_to_xywhn(xywh, image_size)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def xyxyp_to_cxywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    cxywhn = xyxyn_to_cxywhn(xyxyn)
    return cxywhn


def xywhp_to_cxywhn(xywhp):
    xywhn = xywhp_to_xywhn(xywhp)
    cxywhn = xywhn_to_cxywhn(xywhn)
    return cxywhn


def xyxy_to_cxywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywh_to_cxywhp(xywh, image_size):
    xywhp = xywh_to_xywhp(xywh, image_size)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def xyxyn_to_cxywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    cxywhp = xyxyp_to_cxywhp(xyxyp)
    return cxywhp


def xywhn_to_cxywhp(xywhn):
    xywhp = xywhn_to_xywhp(xywhn)
    cxywhp = xywhp_to_cxywhp(xywhp)
    return cxywhp


def cxywhp_to_xywh(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh


def xyxyp_to_xywh(xyxyp, image_size):
    xyxy = xyxyp_to_xyxy(xyxyp, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def cxywhn_to_xywh(cxywhn, image_size):
    cxywh = cxywhn_to_cxywh(cxywhn, image_size)
    xywh = cxywh_to_xywh(cxywh)
    return xywh


def xyxyn_to_xywh(xyxyn, image_size):
    xyxy = xyxyn_to_xyxy(xyxyn, image_size)
    xywh = xyxy_to_xywh(xyxy)
    return xywh


def xyxy_to_xywhn(xyxy, image_size):
    xyxyn = xyxy_to_xyxyn(xyxy, image_size)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def cxywh_to_xywhn(cxywh, image_size):
    cxywhn = cxywh_to_cxywhn(cxywh, image_size)
    xywhn = cxywhn_to_xywhn(cxywhn)
    return xywhn


def xyxyp_to_xywhn(xyxyp):
    xyxyn = xyxyp_to_xyxyn(xyxyp)
    xywhn = xyxyn_to_xywhn(xyxyn)
    return xywhn


def cxywhp_to_xywhn(cxywhp):
    cxywhp = cxywhp_to_cxywhn(cxywhp)
    xywhn = cxywhn_to_xywhn(cxywhp)
    return xywhn


def xyxy_to_xywhp(xyxy, image_size):
    xyxyp = xyxy_to_xyxyp(xyxy, image_size)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def xyxyn_to_xywhp(xyxyn):
    xyxyp = xyxyn_to_xyxyp(xyxyn)
    xywhp = xyxyp_to_xywhp(xyxyp)
    return xywhp


def cxywh_to_xywhp(cxywh, image_size):
    cxywhp = cxywh_to_cxywhp(cxywh, image_size)
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp


def cxywhn_to_xywhp(cxywhn):
    cxywhp = cxywhn * 100
    xywhp = cxywhp_to_xywhp(cxywhp)
    return xywhp


def xywhn_to_xyxy(xywhn, image_size):
    xywh = rescale_bounding_boxes(xywhn, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def cxywhn_to_xyxy(cxywhn, image_size):
    cxywh = rescale_bounding_boxes(cxywhn, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def xywhp_to_xyxy(xywhp, image_size):
    xywh = xywhp_to_xywh(xywhp, image_size)
    xyxy = xywh_to_xyxy(xywh)
    return xyxy


def cxywhp_to_xyxy(cxywhp, image_size):
    cxywh = cxywhp_to_cxywh(cxywhp, image_size)
    xyxy = cxywh_to_xyxy(cxywh)
    return xyxy


def xywh_to_xyxyn(xywh, image_size):
    xywhn = normalize_bounding_boxes(xywh, image_size)
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def cxywh_to_xyxyn(cxywh, image_size):
    cxywhn = normalize_bounding_boxes(cxywh, image_size)
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def xywhp_to_xyxyn(xywhp):
    xywhn = xywhp / 100
    xyxyn = xywhn_to_xyxyn(xywhn)
    return xyxyn


def cxywhp_to_xyxyn(cxywhp):
    cxywhn = cxywhp / 100
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    return xyxyn


def xywh_to_xyxyp(xywh, image_size):
    xyxyn = xywh_to_xyxyn(xywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def xywhn_to_xyxyp(xywhn):
    xyxyn = xywhn_to_xyxyn(xywhn)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywh_to_xyxyp(cxywh, image_size):
    xyxyn = cxywh_to_xyxyn(cxywh, image_size)
    xyxyp = xyxyn * 100
    return xyxyp


def cxywhn_to_xyxyp(cxywhn):
    xyxyn = cxywhn_to_xyxyn(cxywhn)
    xyxyp = xyxyn * 100
    return xyxyp
