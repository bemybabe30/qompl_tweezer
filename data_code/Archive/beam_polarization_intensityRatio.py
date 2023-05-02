import cv2 as cv
import numpy as np
from image_process import *
from functions import *
from fitting import *
import matplotlib.pyplot as plt

position = "long"
input_data1 = r'/Users/leeyongwoong/Documents/downloads/drive-download-20221114T144910Z-001/s-pol_LP_angle40.tif'.format(position)
input_data2 = r'/Users/leeyongwoong/Documents/downloads/drive-download-20221114T144910Z-001/s-pol_LP_angle130.tif'.format(position)


img1 = cv.imread(input_data1, cv.IMREAD_GRAYSCALE)

data1 = np.sum(img1, axis=0)

A = np.max(data1)-np.min(data1)

img2 = cv.imread(input_data2, cv.IMREAD_GRAYSCALE)

data2 = np.sum(img2, axis=0)

B = np.max(data2)-np.min(data2)

Intensity_Ratio = abs(10*np.log(A/B))


print('')
print(A)
print(B)
print('')
print('Intensity ratio')
print(F'The Intensity Ratio(dBm) is {Intensity_Ratio:.6f}.')

#data1
x_hor1 = np.linspace(0, 2447, 2448)
x_ver1 = np.linspace(0, 2047, 2048)
y_hor1 = NormalizeData(input_data1, 0)
y_ver1 = NormalizeData(input_data1, 1)

#data2
x_hor2 = np.linspace(0, 2447, 2448)
x_ver2 = np.linspace(0, 2047, 2048)
y_hor2 = NormalizeData(input_data2, 0)
y_ver2 = NormalizeData(input_data2, 1)

#수평축
plt.plot(x_hor1, y_hor1, '--',color='blue', label='LP angle 90')
plt.plot(x_hor2, y_hor2, '--',color='red', label='LP angle 0')
plt.title('S-pol'.format(position))
plt.xlabel('Pixels')
plt.ylabel('Normalized Intensity')
plt.legend()
plt.grid()
#plt.show()