#!/usr/bin/env python3
""" clasification NeuralNetwork """

import numpy as np


class NeuralNetwork():
    """ w1:
        b1:
        A1:
        W2:
        b2:
        A2:
    """
    def __init__(self, nx, nodes):
        """function initial"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """ The weights vector for the hidden layer """
        return self.__W1

    @property
    def b1(self):
        """ The bias for the hidden layer. """
        return self.__b1

    @property
    def A1(self):
        """  The activated output for the hidden layer. """
        return self.__A1

    @property
    def W2(self):
        """ The weights vector for the output neuron. """
        return self.__W2

    @property
    def b2(self):
        """ The bias for the output neuron """
        return self.__b2

    @property
    def A2(self):
        """ The activated output for the output neuron (prediction) """
        return self.__A2

    def forward_prop(self, X):
        """ Calculates the forward propagation of the neural network """
        tmpA1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-tmpA1))
        tmpA2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-tmpA2))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """ Calculates the cost of the model using logistic regression """
        tmp = np.sum(Y * np.log(A) + (1 - Y) * (np.log(1.0000001 - A)))
        tot = (-1 / Y.shape[1]) * tmp
        return tot

    def evaluate(self, X, Y):
        """ Evaluates the neural network’s predictions """
        self.forward_prop(X)
        result = np.where(self.__A2 >= 0.5, 1, 0)
        return result, self.cost(Y, self.__A2)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """ Calculates one pass of gradient descent on the neuron """
        self.__W1 = self.W1 - alpha * np.matmul(np.matmul(self.W2.T,
                                                          (A2 - Y)) * A1 *
                                                (1 - A1), X.T) / A2.shape[1]
        self.__b1 = self.b1 - alpha * np.sum(np.matmul(self.W2.T,
                                                       (A2 - Y)) * A1 *
                                             (1 - A1), axis=1,
                                             keepdims=True) / A2.shape[1]
        self.__W2 = self.W2 - alpha * np.matmul(A2 - Y, A1.T) / A2.shape[1]
        self.__b2 = self.b2 - alpha * np.sum(A2 - Y) / A2.shape[1]

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Trains the neuron """
        if type(iterations) is not int:
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        for i in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
        return self.evaluate(X, Y)
