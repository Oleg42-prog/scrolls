import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.representations.normalised import xyxyn_to_xywhn, xyxyn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations.normalised import xywhn_to_xyxyn, xywhn_to_cxywhn
from scrolls.geometry.boxes.convertors.representations.normalised import cxywhn_to_xyxyn, cxywhn_to_xywhn
from tests.geometry.boxes.convertors.ground_truth import normalised as gt


class TestBoxConvertorsNormalisedRepresentationsBase(unittest.TestCase):

    EPS = 1e-6

    def setUp(self):
        self.gt = gt.NORMALISED_UNION_BIRDS

    def test_xyxyn_to_xywhn(self):
        xywhn = xyxyn_to_xywhn(self.gt.xyxyn)
        np.testing.assert_allclose(xywhn, self.gt.xywhn, rtol=self.EPS, atol=self.EPS)

    def test_xyxyn_to_cxywhn(self):
        cxywhn = xyxyn_to_cxywhn(self.gt.xyxyn)
        np.testing.assert_allclose(cxywhn, self.gt.cxywhn, rtol=self.EPS, atol=self.EPS)

    def test_xywhn_to_xyxyn(self):
        xyxyn = xywhn_to_xyxyn(self.gt.xywhn)
        np.testing.assert_allclose(xyxyn, self.gt.xyxyn, rtol=self.EPS, atol=self.EPS)

    def test_xywhn_to_cxywhn(self):
        cxywhn = xywhn_to_cxywhn(self.gt.xywhn)
        np.testing.assert_allclose(cxywhn, self.gt.cxywhn, rtol=self.EPS, atol=self.EPS)

    def test_cxywhn_to_xyxyn(self):
        xyxyn = cxywhn_to_xyxyn(self.gt.cxywhn)
        np.testing.assert_allclose(xyxyn, self.gt.xyxyn, rtol=self.EPS, atol=self.EPS)

    def test_cxywhn_to_xywhn(self):
        xywhn = cxywhn_to_xywhn(self.gt.cxywhn)
        np.testing.assert_allclose(xywhn, self.gt.xywhn, rtol=self.EPS, atol=self.EPS)


class TestBoxConvertorsNormalisedRepresentationsLeft(TestBoxConvertorsNormalisedRepresentationsBase):

    def setUp(self):
        self.gt = gt.NORMALISED_LEFT_BIRD


class TestBoxConvertorsNormalisedRepresentationsRight(TestBoxConvertorsNormalisedRepresentationsBase):

    def setUp(self):
        self.gt = gt.NORMALISED_RIGHT_BIRD


class TestBoxConvertorsNormalisedRepresentationsUnion(TestBoxConvertorsNormalisedRepresentationsBase):

    def setUp(self):
        self.gt = gt.NORMALISED_UNION_BIRDS


if __name__ == '__main__':
    unittest.main()
