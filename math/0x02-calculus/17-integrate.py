#!/usr/bin/env python3
""" integrate """


def poly_integral(poly, C=0):
    """ calculate integral polynomial """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int):
        return None
    if poly == [0]:
        return [C]

    list_new = [C]
    for i in range(1, len(poly)):
        if (poly[i] / (i + 1)).is_integer():
            list_new.append(int(poly[i] / (i + 1)))
        else:
            list_new.append(poly[i] / (i + 1))
    return list_new
