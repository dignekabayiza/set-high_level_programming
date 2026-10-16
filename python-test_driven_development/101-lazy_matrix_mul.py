#!/usr/bin/python3
"""101-lazy_matrix_mul module.

Multiplies two matrices using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Args:
        m_a (list): a list of lists of integers or floats.
        m_b (list): a list of lists of integers or floats.

    Raises:
        Whatever exception NumPy raises when the matrices are invalid
        or can't be multiplied.
    """
    return numpy.matmul(m_a, m_b)
