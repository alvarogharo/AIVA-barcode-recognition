import cv2
import random


class BarcodeRecognizer:

    def __init__(self):
        self._MAX_NUMBER = 999999999999999999

    def recognize(self, image_path):
        image = cv2.imread(image_path)
        barcode_result = random.randint(0, self._MAX_NUMBER)
        return str(barcode_result)
