from .context import src
import unittest
import os


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.FOLDER_PATH = "./tests/images/"
        cls.IMAGE_NAME = "image3.tif"
        cls.BARCODE_ERROR_NAME = "code128.gif"
        cls.IMAGE_PATH = cls.FOLDER_PATH + cls.IMAGE_NAME
        cls.GROUNDTRUTH = 123456784
        cls.GROUNDTRUTHS = [None, 123456789101213, 123456784]

    def setUp(self):
        print('-----------------------------------')
        print('Initializing test')
        self.bar_recognizer = src.BarcodeRecognizer()

    def test_result_type(self):
        """Checks if the obtained result with a correct given path if from type int"""
        barcode_content = self.bar_recognizer.recognize(self.IMAGE_PATH)
        print("Result: " + str(barcode_content))

        self.assertEqual(type(barcode_content), int)

    def test_input_error(self):
        """Checks if the obtained result with an incorrect given path is none"""
        incorrect_path = "nofolder"
        barcode_content = self.bar_recognizer.recognize(incorrect_path)
        print("Result: " + str(barcode_content))

        self.assertEqual(barcode_content, None)

    def test_simple_correct_result(self):
        """Checks if the obtained result with a correct given path is equals to the expected groundtruth"""
        barcode_content = self.bar_recognizer.recognize(self.IMAGE_PATH)
        print("Result: " + str(barcode_content))

        self.assertEqual(barcode_content, self.GROUNDTRUTH)

    def test_correct_result(self):
        """Checks if the obtained result with a correct given path is equals to the expected groundtruth"""
        image_names = os.listdir(self.FOLDER_PATH)
        image_names.sort()
        for i in range(len(image_names)):
            barcode_content = self.bar_recognizer.recognize(self.FOLDER_PATH + image_names[i])
            print("Result: " + str(barcode_content))

            self.assertEqual(barcode_content, self.GROUNDTRUTHS[i])

    def test_barcode_start_error(self):
        """Checks if the barcode start is correct"""
        barcode_content = self.bar_recognizer.recognize(self.BARCODE_ERROR_NAME)
        print("Result: " + str(barcode_content))

        self.assertEqual(barcode_content, None)



if __name__ == '__main__':
    # Test sets
    tests = unittest.TestSuite()
    tests.addTest(Test('test_result_type'))
    tests.addTest(Test('test_input_error'))
    tests.addTest(Test('test_simple_correct_result'))
    tests.addTest(Test('test_correct_result'))
    tests.addTest(Test('test_barcode_start_error'))

    # Test launch
    # unittest.TextTestRunner().run(tests1)
    unittest.main()
