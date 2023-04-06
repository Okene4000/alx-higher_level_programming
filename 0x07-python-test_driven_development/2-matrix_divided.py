#!/usr/bin/python3
"""This function divides all element of a matrix."""

def matrix_divided(matrix, div):
    """
    Divide a matrix number by number.
    matrix: matrix to be divided.
    div: number to divided the matrix.
    """
    newList = []
    if type(div) not in [int, float]:
        raise TypeError("div has to be a number")
    if div == 0:
        raise ZeroDivisionError("divide by zero")
    for i in matrix:
        i = []
        if type(i) is not list:
            raise TypeError("matrix has to be a matrix\
 (list of lists) of integer or float")
        if(len(matrix[0]) != len(i)):
            raise TypeError("Each row of the matrix\
 must be the same size")
        for j in range(len(i)):
            if (type(i[j]) is not int) and (type(i[j]) is not float):
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
            l.append(round(((i[j]) / div), 2))
        newList.append(l)
    return newList
