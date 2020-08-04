#!/usr/bin/env python3
''' func '''


def factorial(n):
    ''' func '''
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


class Poisson:
    ''' func '''
    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        ''' func '''

        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)

        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        ''' func '''

        if k < 0:
            return 0
        if type(k) != int:
            k = int(k)
        return (e**(-self.lambtha) * self.lambtha**k) / factorial(k)

    def cdf(self, k):
        ''' func '''

        if k < 0:
            return 0

        if type(k) != int:
            k = int(k)

        p = 0
        for i in range(k + 1):
            p += ((self.lambtha**i) / factorial(i))

        return e**(-self.lambtha) * p
