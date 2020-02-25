import unittest
import numpy as np


class Test1(unittest.TestCase):
    def test(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        img = np.array(mat, np.uint8)
        res = filter(img)
        self.assertTrue(res[0][0] == 5)


if __name__ == "__main__":
    unittest.main()
