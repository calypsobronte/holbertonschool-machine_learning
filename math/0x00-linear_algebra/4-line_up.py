#!/usr/bin/env python3
""" matrix """


def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    mat1 = []
    for i in range(len(arr1)):
        mat1.append(arr1[i] + arr2[i])

    return mat1
