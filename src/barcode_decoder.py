import cv2
import imutils as imutils
import numpy as np

class BarcodeDecoder:

    def __init__(self):
        self.value = [-1]
        self._BW_THRESHOLD = 50
        self._NUMBER_DECODE_MASKS = [[0, 0, 1, 1, 0],   #0
                                     [1, 0, 0, 0, 1],   #1
                                     [0, 1, 0, 0, 1],   #2
                                     [1, 1, 0, 0, 0],   #3
                                     [0, 0, 1, 0, 1],   #4
                                     [1, 0, 1, 0, 0],   #5
                                     [0, 1, 1, 0, 0],   #6
                                     [0, 0, 0, 1, 1],   #7
                                     [1, 0, 0, 1, 0],   #8
                                     [0, 1, 0, 1, 0]]   #9
        self._BLACK_INDICES = [0, 2, 4, 6, 8]
        self._WHITE_INDICES = [1, 3, 5, 7, 9]

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

        cont_np = np.array(cont)

        if ((cont_np[2:6]<med).all()):
            print("barcode init OK")

            for i in range(6, len(cont_np)-10, 10):
                n = cont_np[i:i+10] > med

                black = np.take(n, self._BLACK_INDICES)
                white = np.take(n, self._WHITE_INDICES)
                for x in range(9):
                    if (self._NUMBER_DECODE_MASKS[x] == black).all():
                        self.value.append(x)
                        break
                for x in range(9):
                    if (self._NUMBER_DECODE_MASKS[x] == white).all():
                        self.value.append(x)
                        break

            print(self.value)
            return self.value
        else:
            print("error in decoder")
            return self.value

        cv2.imshow("rot",img)
        cv2.waitKey(0)



