#!/usr/bin/python3
"""
Provides a function that uses numpy to mutiply
matrices.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using Numpy.

    Args:
        m_a: the first matrix (NumPy array).
        m_b: the second matrix (NumPy array).

    Returns:
        the product of the two matrices as a NumPy array.
    """
    if not isinstance(m_a, np.ndarray) or not isinstance(m_b, np.ndarray):
        raise TypeError("both matrices must be NumPy arrays")

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("columns in m_a must be equal to rows in m_b")

    return np.dot(m_a, m_b)
