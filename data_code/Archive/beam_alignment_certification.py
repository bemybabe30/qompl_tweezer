from image_process import *
import matplotlib.pyplot as plt
from functions import *
from fittings import *
import numpy as np
import cv2 as cv

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for k in range(1, 11):
    for j in range(1, 3):
        if j == 1:
            for i in range(1, 30):
                data = 'D:/experiments_data/2023.05.02/%d/aom%d/aom (%d).tif'%(k, j, i)

                y_hor = NormalizeData(data, 0)
                x_hor = np.linspace(0, 2447, 2448)

                y_zeros = np.zeros(y_hor.size)
                y_zeros  = y_zeros + y_hor

                input_fn = gauss2
                guess = [1, 2000, 200, 0.4, 400, 100]
                par_h, SE_h = fitting_6par(input_fn, x_hor, y_hor, guess)

                sum1 = sum1 + round(3.45*np.sqrt(2)*par_h[2],2)
                sum2 = sum2 + round(3.45*np.sqrt(2)*par_h[5],2)

            average_aom1_0th = round(sum1 / 29, 2)
            average_aom1_1st = round(sum2 / 29, 2)

        else:
            for i in range(1, 30):
                data = 'D:/experiments_data/2023.05.02/%d/aom%d/aom (%d).tif'%(k, j, i)

                y_hor = NormalizeData(data, 0)
                x_hor = np.linspace(0, 2447, 2448)

                y_zeros = np.zeros(y_hor.size)
                y_zeros = y_zeros + y_hor

                input_fn = gauss2
                guess = [1, 2000, 200, 0.4, 400, 100]
                par_h, SE_h = fitting_6par(input_fn, x_hor, y_hor, guess)

                sum3 = sum3 + round(3.45*np.sqrt(2)*par_h[2],2)
                sum4 = sum4 + round(3.45*np.sqrt(2)*par_h[2],2)

            average_aom2_0th = round(sum3 / 29, 2)
            average_aom2_1st = round(sum4 / 29, 2)

    print(average_aom1_0th)
