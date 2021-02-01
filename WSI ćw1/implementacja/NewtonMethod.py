# author: Adam Nowakowski

import numpy as np


class NewtonMethod:

    def __init__(self, function):
        self.function = function

    def solve(self, startPoint, beta):
        x = np.array([startPoint]).T
        points = []
        u = 10
        while u > 0.00001:
            points.append(x)
            fun = self.function(x)
            d = np.linalg.inv(fun.hess) @ fun.grad
            newX = x + beta * d
            k = 0
            for i in range(len(startPoint)):
                k = k + float(newX[i] - x[i])**2
            u = np.sqrt(k)
            x = newX
        return points
