#!/usr/bin/python3
"""Module for square_matrix_simple"""


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    return [[value ** 2 for value in row] for row in matrix]
