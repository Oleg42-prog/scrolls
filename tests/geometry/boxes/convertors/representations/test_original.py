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
        xywh = xyxy_to_xywh(self.gt.xyxy)
        np.testing.assert_allclose(xywh, self.gt.xywh, rtol=self.EPS, atol=self.EPS)

    def test_xyxy_to_cxywh(self):
        cxywh = xyxy_to_cxywh(self.gt.xyxy)
        np.testing.assert_allclose(cxywh, self.gt.cxywh, rtol=self.EPS, atol=self.EPS)

    def test_xywh_to_xyxy(self):
        xyxy = xywh_to_xyxy(self.gt.xywh)
        np.testing.assert_allclose(xyxy, self.gt.xyxy, rtol=self.EPS, atol=self.EPS)

    def test_xywh_to_cxywh(self):
        cxywh = xywh_to_cxywh(self.gt.xywh)
        np.testing.assert_allclose(cxywh, self.gt.cxywh, rtol=self.EPS, atol=self.EPS)

    def test_cxywh_to_xyxy(self):
        xyxy = cxywh_to_xyxy(self.gt.cxywh)
        np.testing.assert_allclose(xyxy, self.gt.xyxy, rtol=self.EPS, atol=self.EPS)

    def test_cxywh_to_xywh(self):
        xywh = cxywh_to_xywh(self.gt.cxywh)
        np.testing.assert_allclose(xywh, self.gt.xywh, rtol=self.EPS, atol=self.EPS)


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
