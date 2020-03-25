import numpy as np

class BarcodeDecoder:

    def __init__(self):
        self._BW_THRESHOLD = 50
        self._NUMBER_DECODE_MASKS = [[0, 0, 1, 1, 0],   # 0
                                     [1, 0, 0, 0, 1],   # 1
                                     [0, 1, 0, 0, 1],   # 2
                                     [1, 1, 0, 0, 0],   # 3
                                     [0, 0, 1, 0, 1],   # 4
                                     [1, 0, 1, 0, 0],   # 5
                                     [0, 1, 1, 0, 0],   # 6
                                     [0, 0, 0, 1, 1],   # 7
                                     [1, 0, 0, 1, 0],   # 8
                                     [0, 1, 0, 1, 0]]   # 9
        self._BLACK_INDICES = [0, 2, 4, 6, 8]
        self._WHITE_INDICES = [1, 3, 5, 7, 9]

    def decode(self, img):
        """
        Decode the barcode of the crop image.
        :param img - Crop image of barcode
        :returns result - Barcode value
        """
        h = img.shape[0]
        w = img.shape[1]

        roi_pos = int(h/2)

        if w < h:                # if the image is vertical it will be rotated
            img = np.rot90(img)
            roi_pos = int(w/2)

        roi = img[roi_pos, :, 0]

        width_counter = self._count(roi)

        max_value = np.amax(width_counter, initial=1)
        roi_pos = int(max_value/2)+1                    # width of the thin and wide bars

        width_counter = np.array(width_counter)

        np_result = self._bar_to_number(width_counter, roi_pos)

        result = self._np_to_int(np_result)

        return result

    def _count(self, roi):
        """
        Count roi values to calculate the width of bars
        :param roi - row to analyze
        :return cont - roi bars width array
        """
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

    def _bar_to_number(self, w_counter, m):
        """
        Decoding from the thickness sequence
        :param w_counter - roi bars width array
        :param: m - average value of the width of the bars
        :return value_array - barcode values numpy array
        """
        value_array = [-1]

        if ((w_counter[1:5]<m).all()):

            for i in range(5, len(w_counter)-10, 10):
                n = w_counter[i:i+10] > m

                black = np.take(n, self._BLACK_INDICES)
                white = np.take(n, self._WHITE_INDICES)
                for x in range(10):
                    if (self._NUMBER_DECODE_MASKS[x] == black).all():
                        value_array.append(x)
                        break
                for x in range(10):
                    if (self._NUMBER_DECODE_MASKS[x] == white).all():
                        value_array.append(x)
                        break
            return value_array
        else:
            print("error in decoder")
            return value_array

    def _np_to_int(self,  num):
        """
        Translation from numpy array to int
        :param num - barcode values numpy array
        :return result - int barcode values
        """
        num = np.delete(num, 0)

        num = [str(i) for i in num]
        result = int("".join(num))

        return result


















