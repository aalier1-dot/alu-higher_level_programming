#!/usr/bin/python3
"""
This module contains the function lazy_matrix_mul(m_a, m_b).
It multiplies two matrices using the numpy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using numpy.
    """
    return np.matmul(m_a, m_b)
