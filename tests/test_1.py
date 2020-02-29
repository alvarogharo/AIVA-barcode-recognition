import unittest
import numpy as np
from .context import src


class Test1(unittest.TestCase):

    def __init__(self, testCase):
        self.IMAGE_PATH = "images/image.jpg"

    def test(self):
        bar_recognizer = src.BarcodeRecognizer()
        barcode_content = bar_recognizer.recognize(self.IMAGE_PATH)

        print(barcode_content)


if __name__ == "__main__":
    unittest.main()
