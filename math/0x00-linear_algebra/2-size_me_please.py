#!/usr/bin/env python3
def matrix_shape(matrix):
    mat1 = []
    mat2 = matrix
    while isinstance(mat2, list):
        mat1.append(len(mat2))
        mat2 = matrix[0]
        matrix = mat2
    return mat1
