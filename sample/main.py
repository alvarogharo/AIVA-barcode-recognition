from sample.barcoderecognizer import BarcodeRecognizer

IMAGE_PATH = "images/image.jpg"

bar_recognizer = BarcodeRecognizer()
barcode_content = bar_recognizer.recognize(IMAGE_PATH)

print(barcode_content)


