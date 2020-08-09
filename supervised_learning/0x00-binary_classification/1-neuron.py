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
        self.__W = np.array([np.random.randn(nx)])
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """  The weights vector for the neuron """
        return self.__W

    @property
    def b(self):
        """ The bias for the neuron """
        return self.__b

    @property
    def A(self):
        """ The activated output of the neuron (prediction). """
        return self.__A
