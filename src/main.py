from .barcode_recognizer import BarcodeRecognizer

bar_recognizer = BarcodeRecognizer()
bar_recognizer.recognize("./images/image1.tif")