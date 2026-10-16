#!/usr/bin/python3
"""101-lazy_matrix_mul module.

Multiplies two matrices using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Raises:
        Whatever exception NumPy raises for invalid matrices.
    """
    return numpy.matmul(m_a, m_b)
