# author: Adam Nowakowski
"""Module with two-dimensional test functions f1 and f2"""

import numpy as np

mi1 = np.array([[14],
                [-11]])
mi2 = np.array([[10],
                [-10]])
mi3 = np.array([[7],
                [-13]])
sigma1 = np.array([[1.3, -0.5],
                   [-0.5, 0.8]])
sigma2 = np.array([[1.7, 0.4],
                   [0.4, 1.2]])
sigma3 = np.array([[1.0, 0.0],
                   [0.0, 1.5]])


def fi(x, mi, sigma):
    """Fi function for f1"""

    numerator = np.exp(-0.5*(x - mi).T @ np.linalg.inv(sigma) @ (x - mi))
    denominator = np.sqrt((2*np.pi)**2*np.linalg.det(sigma))
    return numerator/denominator


def f1(x):
    """Solving f1 for two-dimensional x"""

    out = fi(x, mi1, sigma1) + fi(x, mi2, sigma2) + fi(x, mi3, sigma3)
    return out


def f2(x):
    """Solving f2 for two-dimensional x"""

    out = -20*np.exp(-0.2*np.sqrt(0.5*x.T @ x)) - np.exp(0.5*(np.cos(2*np.pi*float(x[0])) + np.cos(2*np.pi*float(x[1])))) + np.e + 20
    return out


def opposite(fun):
    """
    Gives us -f(x) from f(x)

    :param fun: function to convert
    :return:
    """

    def ops(x):
        return -fun(x)
    return ops
