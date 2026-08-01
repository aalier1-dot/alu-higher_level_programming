#!/usr/bin/python3
"""
This module contains the function matrix_divided(matrix, div).
It divides every element of a matrix by div, rounding each
result to 2 decimal places, and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for elem in row:
            if isinstance(elem, bool) or not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
