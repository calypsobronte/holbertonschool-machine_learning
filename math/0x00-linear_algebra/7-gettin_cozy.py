#!/usr/bin/env python3
""" matrix """


def cat_matrices2D(mat1, mat2, axis=0):
    """ matrix """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return
        return [[i for i in j] for j in mat1] +\
               [[i for i in j] for j in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return
        return [[[i for i in j] for j in mat1][i] +
                [[i for i in j] for j in mat2][i]
                for i in range(len([[i for i in j] for j in mat1]))]
