from image_process import *
from functions import *
from fittings import *
import matplotlib.pyplot as plt

position = "110cm"
input_data = r'/Users/leeyongwoong/Library/Mobile Documents/com~apple~CloudDocs/학교 관련 자료/Quantum optics Lab/실험 자료/2022.11.18/beam_size.tif'.format(position)

x_hor = np.linspace(0, 2447, 2448)
x_ver = np.linspace(0, 2047, 2048)
y_hor = get_data(input_data, 0)
y_ver = get_data(input_data, 1)
input_fn = gauss

strh = 0
stph = 2400
strv = 0
stpv = 2000
xh_range = np.linspace(strh, stph, stph - strh + 1)
yh_range = y_hor[strh:stph + 1]
xv_range = np.linspace(strv, stpv, stpv - strv + 1)
yv_range = y_ver[strv:stpv + 1]
guess_hor = [146600, 1250, 1050, 0, 0]
guess_ver = [155500, 1000, 1100, 0, 0]

par_h, SE_h = fitting_5par(input_fn, xh_range, yh_range, guess_hor)
fit_yhor = input_fn(xh_range, par_h[0], par_h[1], par_h[2], par_h[3], par_h[4])

par_v, SE_v = fitting_5par(input_fn, xv_range, yv_range, guess_ver)
fit_yver = input_fn(xv_range, par_v[0], par_v[1], par_v[2], par_v[3], par_v[4])

print('')
print('Horizontal fitting parameters')
print(F'The value of A is {par_h[0]:.6f} with standard error of {SE_h[0]:.6f}.')
print(F'The value of B is {par_h[1]:.6f} with standard error of {SE_h[1]:.6f}.')
print(F'The value of C is {par_h[2]:.6f} with standard error of {SE_h[2]:.6f}.')
print(F'The value of D is {par_h[3]:.6f} with standard error of {SE_h[3]:.6f}.')
print(F'The value of E is {par_h[4]:.6f} with standard error of {SE_h[4]:.6f}.')
print('')
print('Vertical fitting parameters')
print(F'The value of A is {par_v[0]:.6f} with standard error of {SE_v[0]:.6f}.')
print(F'The value of B is {par_v[1]:.6f} with standard error of {SE_v[1]:.6f}.')
print(F'The value of C is {par_v[2]:.6f} with standard error of {SE_v[2]:.6f}.')
print(F'The value of D is {par_v[3]:.6f} with standard error of {SE_v[3]:.6f}.')
print(F'The value of E is {par_v[4]:.6f} with standard error of {SE_v[4]:.6f}.')
print('')
print('Beam size estimation')
print(F'The value of w_hor(mm) @{position} is {par_h[2] * 0.00345:.6f} with standard error of {SE_h[2] * 0.00345:.6f}.')
print(F'The value of w_ver(mm) @{position} is {par_v[2] * 0.00345:.6f} with standard error of {SE_v[2] * 0.00345:.6f}.')

plt.plot(x_hor, y_hor, '.', label='data')
plt.plot(xh_range, fit_yhor, '-', label='fit')
plt.title('Intensity vs. Horizontal pixels @{}'.format(position))
plt.xlabel('Pixels')
plt.ylabel('Intensity')
plt.legend()
plt.grid()
plt.show()

plt.plot(x_ver, y_ver, '.', label='data')
plt.plot(xv_range, fit_yver, '-', label='fit')
plt.title('Intensity vs. Vertical pixels @{}'.format(position))
plt.xlabel('Pixels')
plt.ylabel('Intensity')
plt.legend()
plt.grid()
plt.show()
