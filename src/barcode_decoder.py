import cv2
import imutils as imutils
import numpy as np

class BarcodeDecoder:

    def __init__(self):
        self.value = -1

    def decoder(self, img):
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
        print(range(roi_1.shape[0]))
        for r in range(roi_1.shape[0]):
            print(roi_1[r])
            if roi_1[r]>50 and init == False:
                cont.append(-1)
                init = True

            if init:
                if roi_1[r] >= 50:
                    if last_value == False:
                        cont.append(1)
                        last_value = True
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

                if roi_1[r] < 50:
                    if last_value == True:
                        cont.append(1)
                        last_value = False
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

        print(roi_1)
        print(cont)
        cv2.imshow("rot",img)
        cv2.waitKey(0)



