from .barcode_recognizer import BarcodeRecognizer
from .barcode_decoder import BarcodeDecoder
import cv2

bar_recognizer = BarcodeRecognizer()
bar_decoder = BarcodeDecoder()
original_img, crop_img, rect = bar_recognizer.recognize("./images/image3.tif")
cv2.imshow("Test1", crop_img)
cv2.waitKey(0)
val = bar_decoder.decoder(crop_img)

