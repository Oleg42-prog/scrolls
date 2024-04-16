import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh
from tests.geometry.boxes.convertors import ground_truth as gt


class TestBoxConvertorsOriginalRepresentationsBase(unittest.TestCase):

    EPS = 1e-6

    def setUp(self):
        self.gt = gt.UNION_BIRDS

    def test_xyxy_to_xywh(self):
        xywh_gt = self.gt.xywh
        xyxy = self.gt.xyxy
        xywh = xyxy_to_xywh(xyxy)
        np.testing.assert_allclose(xywh, xywh_gt, rtol=self.EPS, atol=self.EPS)

    def test_xyxy_to_cxywh(self):
        cxywh_gt = self.gt.cxywh
        xyxy = self.gt.xyxy
        cxywh = xyxy_to_cxywh(xyxy)
        np.testing.assert_allclose(cxywh, cxywh_gt, rtol=self.EPS, atol=self.EPS)

    def test_xywh_to_xyxy(self):
        xyxy_gt = self.gt.xyxy
        xywh = self.gt.xywh
        xyxy = xywh_to_xyxy(xywh)
        np.testing.assert_allclose(xyxy, xyxy_gt, rtol=self.EPS, atol=self.EPS)

    def test_xywh_to_cxywh(self):
        cxywh_gt = self.gt.cxywh
        xywh = self.gt.xywh
        cxywh = xywh_to_cxywh(xywh)
        np.testing.assert_allclose(cxywh, cxywh_gt, rtol=self.EPS, atol=self.EPS)

    def test_cxywh_to_xyxy(self):
        xyxy_gt = self.gt.xyxy
        cxywh = self.gt.cxywh
        xyxy = cxywh_to_xyxy(cxywh)
        np.testing.assert_allclose(xyxy, xyxy_gt, rtol=self.EPS, atol=self.EPS)

    def test_cxywh_to_xywh(self):
        xywh_gt = self.gt.xywh
        cxywh = self.gt.cxywh
        xywh = cxywh_to_xywh(cxywh)
        np.testing.assert_allclose(xywh, xywh_gt, rtol=self.EPS, atol=self.EPS)


class TestBoxConvertorsOriginalRepresentationsLeft(TestBoxConvertorsOriginalRepresentationsBase):

    def setUp(self):
        self.gt = gt.LEFT_BIRD


class TestBoxConvertorsOriginalRepresentationsRight(TestBoxConvertorsOriginalRepresentationsBase):

    def setUp(self):
        self.gt = gt.RIGHT_BIRD


class TestBoxConvertorsOriginalRepresentationsUnion(TestBoxConvertorsOriginalRepresentationsBase):

    def setUp(self):
        self.gt = gt.UNION_BIRDS


if __name__ == '__main__':
    unittest.main()
