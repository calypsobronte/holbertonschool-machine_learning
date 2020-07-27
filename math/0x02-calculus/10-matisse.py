#!/usr/bin/env python3
""" derivative """


def poly_derivative(poly):
    """ derive happiness """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    deriv = []
    for i in range(1, len(poly)):
        if isinstance(poly[i], (int, float)):
            deriv.append(poly[i] * i)
        else:
            return None
    return deriv
