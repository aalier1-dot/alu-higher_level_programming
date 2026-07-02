#!/usr/bin/python3
"""Module for print_matrix_integer"""


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for row in matrix:
        print(" ".join("{:d}".format(value) for value in row))
