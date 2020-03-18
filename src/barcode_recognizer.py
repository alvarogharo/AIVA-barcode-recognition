import cv2
import random
from barcode_detector import BarcodeDetector


class BarcodeRecognizer:

    def __init__(self):
        self._MAX_NUMBER = 999999999999999999
        self.bar_detector = BarcodeDetector()

    def recognize(self, image_path):
        image = cv2.imread(image_path)
        if image is not None:
            barcode_result = random.randint(0, self._MAX_NUMBER)
        else:
            barcode_result = None
        #return barcode_result
        return self.bar_detector.detect(image_path)
