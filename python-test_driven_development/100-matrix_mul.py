#!/usr/bin/python3
"""100-matrix_mul module.

Multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Args:
        m_a (list): a list of lists of integers or floats.
        m_b (list): a list of lists of integers or floats.

    Raises:
        TypeError: if a matrix is not a valid list of lists of numbers.
        ValueError: if a matrix is empty or they can't be multiplied.
    """
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(mat, list):
            raise TypeError("{} must be a list".format(name))
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        if not all(isinstance(row, list) for row in mat):
            raise TypeError("{} must be a list of lists".format(name))
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        if mat == [] or all(row == [] for row in mat):
            raise ValueError("{} can't be empty".format(name))
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        for row in mat:
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError(
                        "{} should contain only integers or floats".format(
                            name))
    for name, mat in (("m_a", m_a), ("m_b", m_b)):
        for row in mat:
            if len(row) != len(mat[0]):
                raise TypeError(
                    "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][col]
            new_row.append(total)
        result.append(new_row)
    return result
