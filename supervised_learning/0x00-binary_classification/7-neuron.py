#!/usr/bin/env python3
""" clasification """

import numpy as np
import matplotlib.pyplot as plt


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

    def forward_prop(self, X):
        """ propagation of neuron """
        tmp = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-tmp))
        return self.__A

    def cost(self, Y, A):
        """ Calculates the cost of the model using logistic regression"""
        tmp = np.sum(Y * np.log(A) + (1 - Y) * (np.log(1.0000001 - A)))
        tot = (-1 / Y.shape[1]) * tmp
        return tot

    def evaluate(self, X, Y):
        """ Evaluates the neuron’s predictions """
        self.__A = self.forward_prop(X)
        result = np.where(self.__A >= 0.5, 1, 0)
        return (result, self.cost(Y, self.__A))

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """ Calculates one pass of gradient descent on the neuron """
        self.__W = self.W - (alpha * (np.matmul(X,
                                                (A - Y).transpose()) /
                                      X.shape[1]).transpose())
        self.__b = self.__b - (alpha * (A - Y).sum() / X.shape[1])

    def train(self, X, Y,
              iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """ Trains the neuron """
        if type(iterations) is not int:
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        cost = []
        for i in range(1 + iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            cost.append(self.cost(Y, self.__A))
            print("Cost after {} iterations: {}"
                  .format(i, self.cost(Y, self.__A)))

        plt.plot(np.arange(0, iterations + 1), cost)
        plt.xlabel("iteration")
        plt.ylabel("cost")
        plt.title("Training Cost")
        plt.show()
        return self.evaluate(X, Y)
