from barcode_recognizer import BarcodeRecognizer
import cv2

bar_recognizer = BarcodeRecognizer()
original_img, crop_img, rect = bar_recognizer.recognize("./images/image1.tif")
cv2.imshow("Test1", crop_img)
cv2.waitKey(0)