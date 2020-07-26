#!/usr/bin/env python3
""" sum total of all the decisions """


def summation_i_squared(n):
    """ calculates """

    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * ((n * 2) + 1) // 6
