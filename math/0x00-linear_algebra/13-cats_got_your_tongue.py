#!/usr/bin/env python3
""" matrix """

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ matrix """
    return np.concatenate((mat1, mat2), axis)
