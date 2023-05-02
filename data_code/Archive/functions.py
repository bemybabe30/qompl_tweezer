import scipy.special as sp
import numpy as np


def erf_up(x, A, B, C, D):
    y = A * (1 + sp.erf(np.sqrt(2) * ((x - B) / C))) + D
    return y


def erf_down(x, A, B, C, D):
    y = A * (1 - sp.erf(np.sqrt(2) * ((x - B) / C))) + D
    return y

def gauss(x, A, B, C, D, E):
    y = A * np.exp((-2) * (x - B)**2 / C**2) + D * x + E
    return y

def waist(x, A, B):
    y = A * np.sqrt(1 + (((x - B) * 0.359 / (np.pi * (A ** 2))) ** 2))
    return y

def lorentz(x, A, B, C, D, E):
    gamma = C / 2
    y = A * (gamma ** 2) / (((x - B) ** 2) + (gamma ** 2)) + D * x + E
    return y

def gauss2(x, A, B, C, D, E, F):
    y = A * np.exp(-(x - B)**2 / (2*C**2)) + D * np.exp(-(x - E)**2 / (2*F**2))
    return y

def gauss3(x, A, B, C, D, E, F, G, H, I):
    y = A * np.exp(-(x - B)**2 / (2*C**2)) + D * np.exp(-(x - E)**2 / (2*F**2)) + G * np.exp(-(x - H)**2 / (2*I**2))
    return y

def exponential(x,a,b):
    y = a*np.exp(-b*x)
    return y