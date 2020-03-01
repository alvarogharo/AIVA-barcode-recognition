from .context import src
import unittest
import os


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.FOLDER_PATH = "./tests/images/"
        cls.IMAGE_NAME = "image1.tif"
        cls.IMAGE_PATH = cls.FOLDER_PATH + cls.IMAGE_NAME
        cls.GROUNDTRUTH = 6546546784347
        cls.GROUNDTRUTHS = [6546546784347, 6546546784347, 6546546784347, 6546546784347, 6546546784347, 6546546784347]

    def setUp(self):
        print('-----------------------------------')
        print('Initializing test')
        self.bar_recognizer = src.BarcodeRecognizer()

    #Checks if the obtained result with a correct given path if from type int
    def test_result_type(self):
        barcode_content = self.bar_recognizer.recognize(self.IMAGE_PATH)
        print("Result: " + str(barcode_content))

        self.assertEqual(type(barcode_content), int)

    # Checks if the obtained result with an incorrect given path is none
    def test_input_error(self):
        incorrect_path = "nofolder"
        barcode_content = self.bar_recognizer.recognize(incorrect_path)
        print("Result: " + str(barcode_content))

        self.assertEqual(barcode_content, None)

    # Checks if the obtained result with a correct given path is equals to the expected groundtruth
    def test_correct_result(self):
        image_names = os.listdir(self.FOLDER_PATH)
        image_names.sort()
        for i in range(len(image_names)):
            barcode_content = self.bar_recognizer.recognize(self.FOLDER_PATH + image_names[i])
            print("Result: " + str(barcode_content))

            self.assertEqual(barcode_content, self.GROUNDTRUTHS[i])



if __name__ == '__main__':
    # Test sets
    tests = unittest.TestSuite()
    tests.addTest(Test('test_result_type'))
    tests.addTest(Test('test_input_error'))
    tests.addTest(Test('test_correct_result'))

    # Test launch
    # unittest.TextTestRunner().run(tests1)
    unittest.main()
