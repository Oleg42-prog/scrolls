import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.representations.percentaged import xyxyp_to_xywhp, xyxyp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations.percentaged import xywhp_to_xyxyp, xywhp_to_cxywhp
from scrolls.geometry.boxes.convertors.representations.percentaged import cxywhp_to_xyxyp, cxywhp_to_xywhp
from tests.geometry.boxes.convertors.ground_truth import percentaged as gt


class TestBoxConvertorsPercentagedRepresentationsBase(unittest.TestCase):

    EPS = 1e-6

    def setUp(self):
        self.gt = gt.EMPTY

    def test_xyxyp_to_xywhp(self):
        xywhp = xyxyp_to_xywhp(self.gt.xyxyp)
        np.testing.assert_allclose(xywhp, self.gt.xywhp, rtol=self.EPS, atol=self.EPS)

    def test_xyxyp_to_cxywhp(self):
        cxywhp = xyxyp_to_cxywhp(self.gt.xyxyp)
        np.testing.assert_allclose(cxywhp, self.gt.cxywhp, rtol=self.EPS, atol=self.EPS)

    def test_xywhp_to_xyxyp(self):
        xyxyp = xywhp_to_xyxyp(self.gt.xywhp)
        np.testing.assert_allclose(xyxyp, self.gt.xyxyp, rtol=self.EPS, atol=self.EPS)

    def test_xywhp_to_cxywhp(self):
        cxywhp = xywhp_to_cxywhp(self.gt.xywhp)
        np.testing.assert_allclose(cxywhp, self.gt.cxywhp, rtol=self.EPS, atol=self.EPS)

    def test_cxywhp_to_xyxyp(self):
        xyxyp = cxywhp_to_xyxyp(self.gt.cxywhp)
        np.testing.assert_allclose(xyxyp, self.gt.xyxyp, rtol=self.EPS, atol=self.EPS)

    def test_cxywhp_to_xywhp(self):
        xywhp = cxywhp_to_xywhp(self.gt.cxywhp)
        np.testing.assert_allclose(xywhp, self.gt.xywhp, rtol=self.EPS, atol=self.EPS)


class TestBoxConvertorsPercentagedRepresentationsLeft(TestBoxConvertorsPercentagedRepresentationsBase):

    def setUp(self):
        self.gt = gt.PERCENTAGED_LEFT_BIRD


class TestBoxConvertorsPercentagedRepresentationsRight(TestBoxConvertorsPercentagedRepresentationsBase):

    def setUp(self):
        self.gt = gt.PERCENTAGED_RIGHT_BIRD


class TestBoxConvertorsPercentagedRepresentationsUnion(TestBoxConvertorsPercentagedRepresentationsBase):

    def setUp(self):
        self.gt = gt.PERCENTAGED_UNION_BIRDS


if __name__ == '__main__':
    unittest.main()
