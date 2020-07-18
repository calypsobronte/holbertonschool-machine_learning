#!/usr/bin/env python3
""" matrix """


def np_elementwise(mat1, mat2):
    """ matrix """
    sum = mat1 + mat2
    resta = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return sum, resta, mul, div