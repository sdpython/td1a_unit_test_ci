"""
Functions about polynoms.
"""


def solve_polynom(a, b, c):
    """
    Solve a real polynom of degree 2.

    :param a: coefficient for :math:`x^2`
    :param b: coefficient for :math:`x`
    :param c: coefficient for :math:`1`
    :return: couple of solutions or one if the degree is 1.
    """
    if a == 0:
        # One degree.
        return (-c / b, )
    det = b * b - (4 * a * c)
    if det < 0:
        # No real solution.
        return None

    det = det ** 0.5
    x1 = (b - det) / (2 * a)
    x2 = (b + det) / (2 * a)
    return x1, x2
