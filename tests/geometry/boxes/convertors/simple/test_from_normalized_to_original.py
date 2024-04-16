import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import xyxyn_to_xyxy
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import xywhn_to_xywh
from scrolls.geometry.boxes.convertors.simple.from_normalized_to_original import cxywhn_to_cxywh
import tests.geometry.boxes.convertors.ground_truth.original as gt_o
import tests.geometry.boxes.convertors.ground_truth.normalised as gt_n


class TestBoxSimpleConvertorsFromNormalizedToOriginal(unittest.TestCase):

    EPS = 1e-6

    def setUp(self):
        self.gt_o = gt_o.EMPTY
        self.gt_n = gt_n.EMPTY

    def test_xyxyn_to_xyxy(self):
        xyxy = xyxyn_to_xyxy(self.gt_n.xyxyn, (self.gt_n.original_width, self.gt_n.original_height))
        np.testing.assert_allclose(xyxy, self.gt_o.xyxy, rtol=self.EPS, atol=self.EPS)

    def test_xywhn_to_xywh(self):
        xywh = xywhn_to_xywh(self.gt_n.xywhn, (self.gt_n.original_width, self.gt_n.original_height))
        np.testing.assert_allclose(xywh, self.gt_o.xywh, rtol=self.EPS, atol=self.EPS)

    def test_cxywhn_to_cxywh(self):
        cxywh = cxywhn_to_cxywh(self.gt_n.cxywhn, (self.gt_n.original_width, self.gt_n.original_height))
        np.testing.assert_allclose(cxywh, self.gt_o.cxywh, rtol=self.EPS, atol=self.EPS)


class TestBoxSimpleConvertorsFromNormalizedToOriginalLeft(TestBoxSimpleConvertorsFromNormalizedToOriginal):

    def setUp(self):
        self.gt_o = gt_o.LEFT_BIRD
        self.gt_n = gt_n.NORMALISED_LEFT_BIRD


class TestBoxSimpleConvertorsFromNormalizedToOriginalRight(TestBoxSimpleConvertorsFromNormalizedToOriginal):

    def setUp(self):
        self.gt_o = gt_o.RIGHT_BIRD
        self.gt_n = gt_n.NORMALISED_RIGHT_BIRD


class TestBoxSimpleConvertorsFromNormalizedToOriginalUnion(TestBoxSimpleConvertorsFromNormalizedToOriginal):

    def setUp(self):
        self.gt_o = gt_o.UNION_BIRDS
        self.gt_n = gt_n.NORMALISED_UNION_BIRDS


if __name__ == '__main__':
    unittest.main()
