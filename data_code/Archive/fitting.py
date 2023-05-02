from scipy.optimize import curve_fit
import numpy as np


def fitting_2par(input_fn, x, y):
    xdata = x
    ydata = y
    parameters, covariance = curve_fit(input_fn, xdata, ydata)
    fit_A = parameters[0]
    fit_B = parameters[1]
    SE = np.sqrt(np.diag(covariance))
    SE_A = SE[0]
    SE_B = SE[1]
    return np.array([fit_A, fit_B]), np.array([SE_A, SE_B])

def fitting_2parb(input_fn, x, y, guess, bound):
    xdata = x
    ydata = y
    parameters, covariance = curve_fit(input_fn, xdata, ydata, p0=guess, bounds=bound)
    fit_A = parameters[0]
    fit_B = parameters[1]
    SE = np.sqrt(np.diag(covariance))
    SE_A = SE[0]
    SE_B = SE[1]
    return np.array([fit_A, fit_B]), np.array([SE_A, SE_B])

def fitting_4par(input_fn, x, y):
    xdata = x
    ydata = y
    parameters, covariance = curve_fit(input_fn, xdata, ydata, check_finite=False)
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    SE = np.sqrt(np.diag(covariance))
    SE_A = SE[0]
    SE_B = SE[1]
    SE_C = SE[2]
    SE_D = SE[3]
    return np.array([fit_A, fit_B, fit_C, fit_D]), np.array([SE_A, SE_B, SE_C, SE_D])

def fitting_5par(input_fn, x, y, guess):
    xdata = x
    ydata = y
    parameters, covariance = curve_fit(input_fn, xdata, ydata, p0=guess)
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    fit_E = parameters[4]
    SE = np.sqrt(np.diag(covariance))
    SE_A = SE[0]
    SE_B = SE[1]
    SE_C = SE[2]
    SE_D = SE[3]
    SE_E = SE[4]
    return np.array([fit_A, fit_B, fit_C, fit_D, fit_E]), np.array([SE_A, SE_B, SE_C, SE_D, SE_E])
