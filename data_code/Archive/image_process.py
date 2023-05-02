import cv2 as cv
import numpy as np
def get_data(input_data, a):
    img = cv.imread(input_data, cv.IMREAD_GRAYSCALE)
    data = np.sum(img, axis=a)
    return data

def NormalizeData(input_data, a):
    img = cv.imread(input_data, cv.IMREAD_GRAYSCALE)
    data = np.sum(img, axis=a)
    return (data - np.min(data)) / (np.max(data) - np.min(data))


