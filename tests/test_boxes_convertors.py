import unittest
import numpy as np
from scrolls.geometry.boxes.convertors.representations.original import xyxy_to_xywh, xyxy_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import xywh_to_xyxy, xywh_to_cxywh
from scrolls.geometry.boxes.convertors.representations.original import cxywh_to_xyxy, cxywh_to_xywh


class TestBoxConvertorsOriginalRepresentations(unittest.TestCase):

    def setUp(self):
        self.left = {
            'xyxy': np.array([151, 62, 386, 527]),
            'xywh': np.array([151, 62, 235, 465]),
            'cxywh': np.array([268.5, 294.5, 235, 465])
        }

        self.right = {
            'xyxy': np.array([430, 88, 962, 503]),
            'xywh': np.array([430, 88, 532, 415]),
            'cxywh': np.array([696, 295.5, 532, 415])
        }

        self.union = {
            'xyxy': np.vstack([self.left['xyxy'], self.right['xyxy']]),
            'xywh': np.vstack([self.left['xywh'], self.right['xywh']]),
            'cxywh': np.vstack([self.left['cxywh'], self.right['cxywh']])
        }

    def test_xyxy_to_xywh(self):
        xywh_gt = self.union['xywh']

        xyxy = self.union['xyxy']
        xywh = xyxy_to_xywh(xyxy)

        self.assertEqual(xyxy.shape, xywh_gt.shape)
        self.assertEqual(xywh.shape, xywh_gt.shape)

        for i in range(xywh.shape[0]):
            self.assertAlmostEqual(xywh[i, 0], xywh_gt[i, 0])
            self.assertAlmostEqual(xywh[i, 1], xywh_gt[i, 1])
            self.assertAlmostEqual(xywh[i, 2], xywh_gt[i, 2])
            self.assertAlmostEqual(xywh[i, 3], xywh_gt[i, 3])

    def test_xyxy_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xyxy = self.union['xyxy']
        cxywh = xyxy_to_cxywh(xyxy)

        self.assertEqual(xyxy.shape, cxywh_gt.shape)
        self.assertEqual(cxywh.shape, cxywh_gt.shape)

        for i in range(cxywh.shape[0]):
            self.assertAlmostEqual(cxywh[i, 0], cxywh_gt[i, 0])
            self.assertAlmostEqual(cxywh[i, 1], cxywh_gt[i, 1])
            self.assertAlmostEqual(cxywh[i, 2], cxywh_gt[i, 2])
            self.assertAlmostEqual(cxywh[i, 3], cxywh_gt[i, 3])

    def test_xywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        xywh = self.union['xywh']
        xyxy = xywh_to_xyxy(xywh)

        self.assertEqual(xywh.shape, xyxy_gt.shape)
        self.assertEqual(xyxy.shape, xyxy_gt.shape)

        for i in range(xyxy.shape[0]):
            self.assertAlmostEqual(xyxy[i, 0], xyxy_gt[i, 0])
            self.assertAlmostEqual(xyxy[i, 1], xyxy_gt[i, 1])
            self.assertAlmostEqual(xyxy[i, 2], xyxy_gt[i, 2])
            self.assertAlmostEqual(xyxy[i, 3], xyxy_gt[i, 3])

    def test_xywh_to_cxywh(self):
        cxywh_gt = self.union['cxywh']

        xywh = self.union['xywh']
        cxywh = xywh_to_cxywh(xywh)

        self.assertEqual(xywh.shape, cxywh_gt.shape)
        self.assertEqual(cxywh.shape, cxywh_gt.shape)

        for i in range(cxywh.shape[0]):
            self.assertAlmostEqual(cxywh[i, 0], cxywh_gt[i, 0])
            self.assertAlmostEqual(cxywh[i, 1], cxywh_gt[i, 1])
            self.assertAlmostEqual(cxywh[i, 2], cxywh_gt[i, 2])
            self.assertAlmostEqual(cxywh[i, 3], cxywh_gt[i, 3])

    def test_cxywh_to_xyxy(self):
        xyxy_gt = self.union['xyxy']

        cxywh = self.union['cxywh']
        xyxy = cxywh_to_xyxy(cxywh)

        self.assertEqual(cxywh.shape, xyxy_gt.shape)
        self.assertEqual(xyxy.shape, xyxy_gt.shape)

        for i in range(xyxy.shape[0]):
            self.assertAlmostEqual(xyxy[i, 0], xyxy_gt[i, 0])
            self.assertAlmostEqual(xyxy[i, 1], xyxy_gt[i, 1])
            self.assertAlmostEqual(xyxy[i, 2], xyxy_gt[i, 2])
            self.assertAlmostEqual(xyxy[i, 3], xyxy_gt[i, 3])

    def test_cxywh_to_xywh(self):
        xywh_gt = self.union['xywh']

        cxywh = self.union['cxywh']
        xywh = cxywh_to_xywh(cxywh)

        self.assertEqual(cxywh.shape, xywh_gt.shape)
        self.assertEqual(xywh.shape, xywh_gt.shape)

        for i in range(xywh.shape[0]):
            self.assertAlmostEqual(xywh[i, 0], xywh_gt[i, 0])
            self.assertAlmostEqual(xywh[i, 1], xywh_gt[i, 1])
            self.assertAlmostEqual(xywh[i, 2], xywh_gt[i, 2])
            self.assertAlmostEqual(xywh[i, 3], xywh_gt[i, 3])


if __name__ == '__main__':
    unittest.main()
