from .barcode_recognizer import BarcodeRecognizer

bar_recognizer = BarcodeRecognizer()

decoded_value = bar_recognizer.recognize("./images/image3.tif", show_images=True)
print(decoded_value)

