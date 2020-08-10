#!/usr/bin/env python3
""" clasification """

import numpy as np


class DeepNeuralNetwork:
    """ L:
        cache:
        weights:
    """
    def __init__(self, nx, layers):
        """function initial"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or not layers:
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(self.L):
            if type(layers[i]) != int or layers[i] < 1:
                raise TypeError("layers must be a list of positive integers")
            self.weights["W{}".format(i + 1)] = (np.random.randn(
                layers[i], nx) * np.sqrt(2./nx))
            nx = layers[i]
            self.weights["b{}".format(i + 1)] = np.zeros((layers[i], 1))
