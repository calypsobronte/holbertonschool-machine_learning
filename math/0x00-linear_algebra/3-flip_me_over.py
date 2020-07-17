#!/usr/bin/env python3
""" matrix """


def matrix_transpose(matrix):
    mat1 = []
    for i in range(len(matrix[0])):
        mat2 = [0] * len(matrix)
        mat1.append(mat2)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            mat1[j][i] = matrix[i][j]
    return mat1
