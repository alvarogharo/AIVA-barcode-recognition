import cv2
import imutils as imutils
import numpy as np


class BarcodeDetector:

    def __init__(self):
        self._GRAD_THRESHOLD = 120  # Threshold for gradient mask (remove grad noise)
        self._HOR_MARGIN = 12  # Horizontal offset for crop image
        self._VERT_MARGIN = 10  # Vertical offset for crop image

    def detect(self, image):
        """
        Detect the barcode of the image_path parameter.
        :param image - Path or image for the image to detect barcode
        :returns original_image, crop_img, rect  - Original image, barcode crop image and rect bbox
        """
        if type(image) == str:
            original_image = cv2.imread(image)
        else:
            original_image = image
        image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        ddepth = cv2.CV_32F
        grad_x = cv2.Sobel(image, ddepth=ddepth, dx=1, dy=0, ksize=-1)
        grad_y = cv2.Sobel(image, ddepth=ddepth, dx=0, dy=1, ksize=-1)

        gradient = cv2.subtract(grad_x, grad_y)  # Gradient module calculation
        gradient = cv2.convertScaleAbs(gradient)  # Gradient module calculation

        blurred = cv2.blur(gradient, (9, 9))  # Blurring to reduce noise
        (_, thresh) = cv2.threshold(blurred, self._GRAD_THRESHOLD, 255, cv2.THRESH_BINARY)  # Threshold reduce noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  # Morphological transformations

        closed = cv2.erode(closed, None, iterations=4)  # Morphological transformations
        closed = cv2.dilate(closed, None, iterations=4)  # Morphological transformations

        cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]  # Finds the biggest BLOB on the image

        rect = cv2.minAreaRect(c)  # Creates bbox
        box = cv2.boxPoints(rect)  # Creates bbox
        box = np.int0(box)  # Creates bbox

        # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

        crop_img = original_image[box[1, 1] - self._VERT_MARGIN:box[0, 1] + self._VERT_MARGIN,
                   box[0, 0] - self._HOR_MARGIN:box[2, 0] + self._HOR_MARGIN]  # Crop image
        # crop_img = self._crop_rect(original_image, rect)   # Crop image
        return original_image, crop_img, rect

    def _crop_rect(self, img, rect):
        """
        Crops image with parameter rect even if rect is rotated
        :param img - Image to crop
        :param rect - Rectangle to crop from img
        :return img_crop - img image cropped
        """
        center, size, angle = rect[0], rect[1], rect[2]
        size = list(size)
        size[0] = size[0] + self._HOR_MARGIN  # Adding offset
        size[1] = size[1] + self._VERT_MARGIN  # Adding offset
        size = tuple(size)
        center, size = tuple(map(int, center)), tuple(map(int, size))  # Params for rotation matrix

        height, width = img.shape[0], img.shape[1]  # Params for rotation matrix

        M = cv2.getRotationMatrix2D(center, angle, 1)  # Creates rotation matrix
        img_rot = cv2.warpAffine(img, M, (width, height))  # Image wrapping with rotation m

        img_crop = cv2.getRectSubPix(img_rot, size, center)  # Image crop

        return img_crop
