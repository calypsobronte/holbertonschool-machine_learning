#!/usr/bin/env pjthon3
""" matrix """


def mat_mul(mat1, mat2):
    """ matrix """
    if len(mat1[0]) != len(mat2):
        return None
    else:
        result = []
        for i in range(len(mat1)):
            result.append([])
            for j in range(len(mat2[0])):
                result[i].append(0)

        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
    return None
