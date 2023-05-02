from image_process import *
import matplotlib.pyplot as plt
from functions import *
from fitting import *
import cv2

position = "110cm"

data = [
f'/Users/leeyongwoong/Library/Mobile Documents/com~apple~CloudDocs/학교 관련 자료/Quantum optics Lab/실험 자료/2022.12.20/{(i+1) * 10}V.tif'.format(position)for i in range(6)
]
x_hor = np.linspace(0, 2447, 2448)
fig, ax = plt.subplots(figsize = (8,8))

for i in data:
    y_hor = NormalizeData(i, 0)

    ax.plot(y_hor)

    input_fn = gauss

    yh_range = y_hor

    guess_hor = [1, 1360, 70, 0, 0]

    par_h1, SE_h1 = fitting_5par(input_fn, x_hor, yh_range, guess_hor)

    fit_yhor = input_fn(x_hor, par_h1[0], par_h1[1], par_h1[2], par_h1[3], par_h1[4])

    print(np.argmax(fit_yhor))


    # fittings
    plt.plot(x_hor, fit_yhor, '--', color='blue', linewidth=1.0, label='fit')

plt.show()

# x_hor = np.linspace(0, 2447, 2448)
# y_hor = NormalizeData(data, 0)
#
# fit_param = [
#     gauss(x) for x in data
# ]

# # data1
# # x_hor1 = np.linspace(0, 2447, 2448)
# # y_hor1 = NormalizeData(input_data1, 0)
# #
# data2
# # x_hor2 = np.linspace(0, 2447, 2448)
# # y_hor2 = NormalizeData(input_data2, 0)
# #
# data3
# # x_hor3 = np.linspace(0, 2447, 2448)
# # y_hor3 = NormalizeData(input_data3, 0)
# #
# data4
# # x_hor4 = np.linspace(0, 2447, 2448)
# # y_hor4 = NormalizeData(input_data4, 0)
# #
# data5
# # x_hor5 = np.linspace(0, 2447, 2448)
# # y_hor5 = NormalizeData(input_data5, 0)
# #
# data6
# # x_hor6 = np.linspace(0, 2447, 2448)
# # y_hor6 = NormalizeData(input_data6, 0)
# #
# data2
# # x_hor7 = np.linspace(0, 2447, 2448)
# # y_hor7 = NormalizeData(input_data7, 0)
# #
# data3
# # x_hor8 = np.linspace(0, 2447, 2448)
# # y_hor8 = NormalizeData(input_data8, 0)
# #
# data4
# # x_hor9 = np.linspace(0, 2447, 2448)
# # y_hor9 = NormalizeData(input_data9, 0)
# #
# # plt.plot(x_hor1, y_hor1, '-', color='red', linewidth=2.0, label='10MHz')
# # plt.plot(x_hor2, y_hor2, '-', color='orange', linewidth=2.0, label='20MHz')
# # plt.plot(x_hor3, y_hor3, '-', color='yellow', linewidth=2.0, label='30MHz')
# # plt.plot(x_hor4, y_hor4, '-', color='green', linewidth=2.0, label='40MHz')
# # plt.plot(x_hor5, y_hor5, '-', color='blue', linewidth=2.0, label='50MHz')
# # plt.plot(x_hor6, y_hor6, '--', color='cyan', linewidth=2.0, label='60MHz')
# # plt.plot(x_hor7, y_hor7, '--', color='violet', linewidth=2.0, label='70MHz')
# # plt.plot(x_hor8, y_hor8, '--', color='purple', linewidth=2.0, label='90MHz')
# # plt.plot(x_hor9, y_hor9, '--', color='pink', linewidth=2.0, label='100MHz')
# #
# # plt.title('Piezo drive voltage dependence'.format(position))
# # plt.xlabel('Pixels')
# # plt.ylabel('Normalized Intensity')
# # plt.legend(prop={'size': 7})
# # plt.grid()
# # plt.show()




