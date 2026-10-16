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
        TypeError: if m_a or m_b is not a list or has non-numbers.
    """
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(mat, list):
            raise TypeError("{} must be a list".format(name))
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        for row in mat:
            if isinstance(row, list):
                for item in row:
                    if not isinstance(item, (int, float)):
                        raise TypeError(
                            "{} should contain only integers or "
                            "floats".format(name))
    return numpy.matmul(m_a, m_b)
