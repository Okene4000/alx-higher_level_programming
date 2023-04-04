#!/usr/bin/python3
"""
Function divides all element of a matrix.
"""

def matrix_divided(matrix, div):
    newList = []
    if type(div) not in [int, float]:
        raise TypeError("div has to be an integer")
    if div == 0:
        raise ZeroDivisionError("division must be by zero")
    for a in matrix:
        a = []
        if type(a) is not list:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integer or float")
        if(len(matrix[0]) != len(a)):
            raise TypeError("Each row of the matrix\
 must have the same size")
        for b in range(len(a)):
            if (type(a[b]) is not int) and (type(a[b]) is not float):
                raise TypeError("matrix must be a matrix\
(list of lists) of integer or float")
            l.append(round(((a[b]) / div), 2))
        newList.append(l)
    return newList
