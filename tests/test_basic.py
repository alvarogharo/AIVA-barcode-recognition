from .context import src
import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.IMAGE_PATH = "images/image.jpg"

    def setUp(self):
        print('Initializing test')
        self.bar_recognizer = src.BarcodeRecognizer()

    def test_1(self):
        barcode_content = self.bar_recognizer.recognize(self.IMAGE_PATH)
        print("Result: " + str(barcode_content))

        self.assertEqual(type(barcode_content), int)


if __name__ == '__main__':
    # Test sets
    tests1 = unittest.TestSuite()
    tests1.addTest(Test('test_1'))

    # Test launch
    # unittest.TextTestRunner().run(tests1)
    unittest.main()
