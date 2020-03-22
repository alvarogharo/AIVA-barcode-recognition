import cv2
import imutils as imutils
import numpy as np

class BarcodeDecoder:

    def __init__(self):
        self.value = [-1]
        self._BW_THRESHOLD = 50

    def decode(self, img):
        h = img.shape[0]
        w = img.shape[1]
        init = False
        last_value = False
        cont = []
        c = 0

        med = int(h/2)

        if(w<h):
            #rotate
            img = np.rot90(img)
            med = int(w/2)

        roi_1 = img[med,:,0]

        for r in range(roi_1.shape[0]):
            if roi_1[r]>self._BW_THRESHOLD and init == False:
                cont.append(-1)
                init = True

            if init:
                if roi_1[r] >= self._BW_THRESHOLD:
                    if last_value == False:
                        cont.append(1)
                        last_value = True
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

                if roi_1[r] < self._BW_THRESHOLD:
                    if last_value == True:
                        cont.append(1)
                        last_value = False
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

        max_value = np.amax(cont, initial=2)
        med = int(max_value/2)

        if(np.greater_equal(cont[2:5],med)).all:
            print("barcode init OK")


        else:
            print("error in decoder")
            return self.value

        print(cont)
        cv2.imshow("rot",img)
        cv2.waitKey(0)



