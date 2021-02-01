# author: Adam Nowakowski

import numpy as np


class Fun1:
    def __init__(self, x):
        self.v = x
        self.vDim = len(x)
        i = np.eye(self.vDim)
        self.fun = -self.v.T @ self.v
        self.grad = -2*self.v
        self.hess = -2*i


class Fun2:
    def __init__(self, x):
        self.v = x
        self.vDim = len(x)
        i = np.eye(self.vDim)
        self.fun = -self.v.T @ self.v + 1.1*np.cos(self.v.T @ self.v)
        self.grad = -2*self.v - 2.2*self.v*np.sin(self.v.T @ self.v)
        self.hess = -2*i - 2.2*i*np.sin(self.v.T@self.v) - 4.4*self.v@self.v.T*np.cos(self.v.T@self.v)
