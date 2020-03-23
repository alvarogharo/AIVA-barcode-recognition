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

        med = int(h/2)

        if(w<h):
            #rotate
            img = np.rot90(img)
            med = int(w/2)

        roi_1 = img[med, :, 0]

        width_counter = self._count_(roi_1)

        max_value = np.amax(width_counter, initial=1)
        med = int(max_value/2)+1

        width_counter = np.array(width_counter)

        print(width_counter)

        np_result = self._decodification_(width_counter, med)

        print(np_result)

        result = self._np2int_(np_result)

        print(result)

        self.value = [-1]
        return result



    def _count_(self, roi):
        c = 0
        init = False
        last_value = True
        cont = []

        for r in range(roi.shape[0]):
            if roi[r] < self._BW_THRESHOLD and init == False:
                cont.append(-1)
                init = True

            if init:
                if roi[r] >= self._BW_THRESHOLD:
                    if not last_value:
                        cont.append(1)
                        last_value = True
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

                if roi[r] < self._BW_THRESHOLD:
                    if last_value:
                        cont.append(1)
                        last_value = False
                        c = c+1
                    else:
                        cont[c] = cont[c]+1

        return cont

    def _decodification_(self, w_counter, m):
        if ((w_counter[1:5]<m).all()):

            for i in range(5, len(w_counter)-10, 10):
                n = w_counter[i:i+10] > m

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
            return self.value
        else:
            print("error in decoder")
            return self.value

    def _np2int_(self,  num):
        num = np.delete(num, len(num)-1)
        num = np.delete(num, 0)

        num = [str(i) for i in num]
        res = int("".join(num))

        return res


















