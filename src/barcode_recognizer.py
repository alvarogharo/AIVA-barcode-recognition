import cv2
import random
from .barcode_detector import BarcodeDetector
from .barcode_decoder import BarcodeDecoder


class BarcodeRecognizer:

    def __init__(self):
        self._bar_detector = BarcodeDetector()
        self._bar_decoder = BarcodeDecoder()

    def recognize(self, image_path, show_images=False):
        image = cv2.imread(image_path)
        if image is not None:
            original_img, crop_img, rect = self._bar_detector.detect(image_path)
            if show_images:
                cv2.imshow("Test", crop_img)
                cv2.waitKey(0)
            barcode_result = self._bar_decoder.decode(crop_img)
        else:
            barcode_result = None
        return barcode_result
