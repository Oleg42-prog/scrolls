import unittest
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh
from tests.geometry.boxes.convertors import ground_truth as gt


class TestBoxConvertorsOriginalRepresentations(unittest.TestCase):

    def setUp(self):
        self.left = gt.LEFT_BIRD
        self.right = gt.RIGHT_BIRD
        self.union = gt.UNION_BIRDS

    def test_xyxy_to_xywh(self):
        xywh_gt = self.union['xywh']

        xyxy = self.union['xyxy']
        xywh = xyxy_to_xywh(xyxy)

        self.assertEqual(xyxy.shape, xywh_gt.shape)
        self.assertEqual(xywh.shape, xywh_gt.shape)

        for i in range(xywh.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(xywh[i, j], xywh_gt[i, j])

    def test_xyxy_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xyxy = self.union['xyxy']
        cxywh = xyxy_to_cxywh(xyxy)

        self.assertEqual(xyxy.shape, cxywh_gt.shape)
        self.assertEqual(cxywh.shape, cxywh_gt.shape)

        for i in range(cxywh.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(cxywh[i, j], cxywh_gt[i, j])

    def test_xywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        xywh = self.union['xywh']
        xyxy = xywh_to_xyxy(xywh)

        self.assertEqual(xywh.shape, xyxy_gt.shape)
        self.assertEqual(xyxy.shape, xyxy_gt.shape)

        for i in range(xyxy.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(xyxy[i, j], xyxy_gt[i, j])

    def test_xywh_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xywh = self.union['xywh']
        cxywh = xywh_to_cxywh(xywh)

        self.assertEqual(xywh.shape, cxywh_gt.shape)
        self.assertEqual(cxywh.shape, cxywh_gt.shape)

        for i in range(cxywh.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(cxywh[i, j], cxywh_gt[i, j])

    def test_cxywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        cxywh = self.union['cxywh']
        xyxy = cxywh_to_xyxy(cxywh)

        self.assertEqual(cxywh.shape, xyxy_gt.shape)
        self.assertEqual(xyxy.shape, xyxy_gt.shape)

        for i in range(xyxy.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(xyxy[i, j], xyxy_gt[i, j])

    def test_cxywh_to_xywh(self):
        xywh_gt = self.union['xywh']

        cxywh = self.union['cxywh']
        xywh = cxywh_to_xywh(cxywh)

        self.assertEqual(cxywh.shape, xywh_gt.shape)
        self.assertEqual(xywh.shape, xywh_gt.shape)

        for i in range(xywh.shape[0]):
            for j in range(4):
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(xywh[i, j], xywh_gt[i, j])


if __name__ == '__main__':
    unittest.main()
