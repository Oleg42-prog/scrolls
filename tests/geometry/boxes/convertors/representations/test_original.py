import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh
from tests.geometry.boxes.convertors import ground_truth as gt


class TestBoxConvertorsOriginalRepresentations(unittest.TestCase):

    def setUp(self):
        self.eps = 1e-6
        self.left = gt.LEFT_BIRD
        self.right = gt.RIGHT_BIRD
        self.union = gt.UNION_BIRDS

    def test_xyxy_to_xywh(self):
        xywh_gt = self.union['xywh']

        xyxy = self.union['xyxy']
        xywh = xyxy_to_xywh(xyxy)

        np.testing.assert_allclose(xywh, xywh_gt, rtol=self.eps, atol=self.eps)

    def test_xyxy_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xyxy = self.union['xyxy']
        cxywh = xyxy_to_cxywh(xyxy)

        np.testing.assert_allclose(cxywh, cxywh_gt, rtol=self.eps, atol=self.eps)

    def test_xywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        xywh = self.union['xywh']
        xyxy = xywh_to_xyxy(xywh)

        np.testing.assert_allclose(xyxy, xyxy_gt, rtol=self.eps, atol=self.eps)

    def test_xywh_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xywh = self.union['xywh']
        cxywh = xywh_to_cxywh(xywh)

        np.testing.assert_allclose(cxywh, cxywh_gt, rtol=self.eps, atol=self.eps)

    def test_cxywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        cxywh = self.union['cxywh']
        xyxy = cxywh_to_xyxy(cxywh)

        np.testing.assert_allclose(xyxy, xyxy_gt, rtol=self.eps, atol=self.eps)

    def test_cxywh_to_xywh(self):
        xywh_gt = self.union['xywh']

        cxywh = self.union['cxywh']
        xywh = cxywh_to_xywh(cxywh)

        np.testing.assert_allclose(xywh, xywh_gt, rtol=self.eps, atol=self.eps)


if __name__ == '__main__':
    unittest.main()
