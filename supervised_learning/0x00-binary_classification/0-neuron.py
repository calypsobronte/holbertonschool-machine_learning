#!/usr/bin/env python3
""" clasification """

import numpy as np


class Neuron():
    """ w:
        A:
        b:
    """
    def __init__(self, nx):
        """function initial"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        self.W = np.array([np.random.randn(nx)])
        self.b = 0
        self.A = 0
