import numpy as np
import cv2
import base64


def base64_to_image(base64_image):
    jpg_img = base64.b64decode(base64_image)
    lol = np.fromstring(jpg_img, dtype=np.uint8)
    return cv2.imdecode(lol, cv2.IMREAD_COLOR)