import cv2
import imutils as imutils
import numpy as np

class BarcodeDetector:

    def __init__(self):
        self._GRAD_THRESHOLD = 120
        self._HOR_MARGIN = 10
        self._VERT_MARGIN = 10

    def detect(self, image_path):
        original_image = cv2.imread(image_path)
        image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        ddepth = cv2.CV_32F
        grad_x = cv2.Sobel(image, ddepth=ddepth, dx=1, dy=0, ksize=-1)
        grad_y = cv2.Sobel(image, ddepth=ddepth, dx=0, dy=1, ksize=-1)

        gradient = cv2.subtract(grad_x, grad_y)
        gradient = cv2.convertScaleAbs(gradient)

        blurred = cv2.blur(gradient, (9, 9))
        (_, thresh) = cv2.threshold(blurred, self._GRAD_THRESHOLD, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        closed = cv2.erode(closed, None, iterations=4)
        closed = cv2.dilate(closed, None, iterations=4)

        cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

        crop_img = original_image[box[1, 1]-self._VERT_MARGIN:box[0, 1]+self._VERT_MARGIN, box[0, 0]-self._HOR_MARGIN:box[2, 0]+self._HOR_MARGIN]
        #crop_img = self.crop_rect(original_image, rect)
        return original_image, crop_img, rect

    def crop_rect(self, img, rect):
        center, size, angle = rect[0], rect[1], rect[2]
        size = list(size)
        size[0] = size[0] + self._HOR_MARGIN
        size[1] = size[1] + self._VERT_MARGIN
        size = tuple(size)
        center, size = tuple(map(int, center)), tuple(map(int, size))

        height, width = img.shape[0], img.shape[1]

        M = cv2.getRotationMatrix2D(center, angle, 1)
        img_rot = cv2.warpAffine(img, M, (width, height))

        img_crop = cv2.getRectSubPix(img_rot, size, center)

        return img_crop