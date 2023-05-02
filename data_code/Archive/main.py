from image_process import *
import matplotlib.pyplot as plt
from functions import *
from fittings import *


position = "long"
input_data1 = r'C:/Users/QMOPL/Pictures/data/2023.05.02/aom1_#11.tif'.format(
    position)
input_data2 = r'C:/Users/QMOPL/Pictures/data/2023.05.02/aom2_#11.tif'.format(
    position)

# data1
# x_hor1 = np.linspace(0, 1439, 1440)
x_hor1 = np.linspace(0, 2447, 2448)
y_hor1 = NormalizeData(input_data1, 0)

# data2
# x_hor2 = np.linspace(0, 1439, 1440)
x_hor2 = np.linspace(0, 2447, 2448)
y_hor2 = NormalizeData(input_data2, 0)

# gaussian fitting
input_fn = gauss2

# xh_range1 = np.linspace(0, 1439, 1440)
xh_range1 = np.linspace(0, 2447, 2448)
yh_range1 = y_hor1

# xh_range2 = np.linspace(0, 1439, 1440)
xh_range2 = np.linspace(0, 2447, 2448)
yh_range2 = y_hor2
guess_hor = [1, 2000, 200, 0.4, 400, 100]

#par_h1, SE_h1 = fitting_5par(input_fn, xh_range1, yh_range1, guess_hor)
#par_h2, SE_h2 = fitting_5par(input_fn, xh_range2, yh_range2, guess_hor)
par_h1, SE_h1 = fitting_6par(input_fn, xh_range1, yh_range1, guess_hor)
par_h2, SE_h2 = fitting_6par(input_fn, xh_range2, yh_range2, guess_hor)
fit_yhor1 = input_fn(xh_range1, par_h1[0], par_h1[1], par_h1[2], par_h1[3], par_h1[4], par_h1[5])
fit_yhor2 = input_fn(xh_range2, par_h2[0], par_h2[1], par_h2[2], par_h2[3], par_h2[4], par_h2[5])

fig, ax = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1.5]})
plt.subplot(1, 2, 1)
# 수평축
plt.plot(x_hor1, y_hor1, '-', color='blue', linewidth=2.0, label='AOM1')
plt.plot(x_hor2, y_hor2, '-', color='red', linewidth=2.0, label='AOM2')
#fittings
plt.plot(xh_range1, fit_yhor1, '--', color='blue', linewidth=1.0, label='fit')
plt.plot(xh_range2, fit_yhor2, '--', color='red', linewidth=1.0, label='fit')

#labeling
plt.title('Beam overlap'.format(position))
plt.xlabel('Pixels')
plt.ylabel('Normalized Intensity')
plt.legend(prop={'size': 7})
plt.grid()

plt.subplot(1, 2, 2)
plt.xlim([0,1])
plt.ylim([0,14])
plt.axis('off')

plt.plot()
#0th order beam data
plt.text(0, 12, '0th Order beam Info', fontsize=7, fontweight='bold', color='purple')
plt.text(0, 11, 'BeamCenter at 1st AOM: {}\nstandard error: {}'.format(round(par_h1[1],3),round(SE_h1[1],5)), fontsize=7, fontweight='bold')
plt.text(0, 10, 'BeamCenter at 2st AOM: {}\nstandard error: {}'.format(round(par_h2[1],3),round(SE_h2[1],5)), fontsize=7, fontweight='bold')
plt.text(0, 9, 'Waist at 1st AOM: {}um\nstandard error: {}'.format(round(3.45*np.sqrt(2)*par_h1[2],5),round(SE_h1[2],5)), fontsize=7, fontweight='bold')
plt.text(0, 8, 'Waist at 2st AOM: {}um\nstandard error: {}'.format(round(3.45*np.sqrt(2)*par_h2[2],5),round(SE_h2[2],5)), fontsize=7, fontweight='bold')

#1st order beam data
plt.text(0, 7, '1st Order beam Info', fontsize=7, fontweight='bold', color='purple')
plt.text(0, 6, 'BeamCenter at 1st AOM: {}\nstandard error: {}'.format(round(par_h1[4],3),round(SE_h1[4],5)), fontsize=7, fontweight='bold')
plt.text(0, 5, 'BeamCenter at 2st AOM: {}\nstandard error: {}'.format(round(par_h2[4],3),round(SE_h2[4],5)), fontsize=7, fontweight='bold')
plt.text(0, 4, 'Waist at 1st AOM: {}um\nstandard error: {}'.format(round(3.45*np.sqrt(2)*par_h1[5],3),round(SE_h1[5],5)), fontsize=7, fontweight='bold')
plt.text(0, 3, 'Waist at 2st AOM: {}um\nstandard error: {}'.format(round(3.45*np.sqrt(2)*par_h2[5],3),round(SE_h2[5],5)), fontsize=7, fontweight='bold')
plt.text(0, 2, 'Amplitude at 1st AOM: {}\nstandard error: {}'.format(round(par_h1[3],3),round(SE_h1[3],5)), fontsize=7, fontweight='bold')
plt.text(0, 1, 'Amplitude at 2st AOM: {}\nstandard error: {}'.format(round(par_h2[3],3),round(SE_h2[3],5)), fontsize=7, fontweight='bold')
plt.show()
