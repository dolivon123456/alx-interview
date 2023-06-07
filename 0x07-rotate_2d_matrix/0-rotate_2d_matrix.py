#!/usr/bin/python3

"""
This module provides the function `rotate_2d_matrix`
"""


def getNext(a, z, position):
    """
    Returns a tuple of the next position to be used
    """
    # print(position)
    i = position[0]
    j = position[1]
    if i == a and j < z:
        j += 1
        if j >= z:
            j -= 1
            i += 1
        return (i, j)
    if i < z and j == z - 1:
        i += 1
        if i >= z:
            i -= 1
            j -= 1
        return (i, j)
    if i == z - 1 and j >= a:
        j -= 1
        if j < a:
            j += 1
            i -= 1
        return (i, j)
    if j == a and i >= a:
        i -= 1
        if i < a:
            i += 1
            j += 1
        return(i, j)


def rotate_2d_matrix(matrix):
    """
    Driver function for rotating 2D matrix
    """
    if matrix is None:
        return
    if len(matrix) != len(matrix[0]):
        return

    def rotate_2D_matrix(start, stop):
        """
        This function rotates a 2D matrix by 90 degrees
        """
        # print(start, stop)
        if start == stop - 1 or start == stop:
            return
        a, b = start, start
        i, j = getNext(start, stop, (a, b))
        tmp = matrix[a][b]
        n = (((stop - start - 1) * 4) + 1) * (stop - start - 1)
        for k in range(n):
            # print(i, j)
            matrix[i][j], tmp = tmp, matrix[i][j]
            i, j = getNext(start, stop, (i, j))
            a, b = getNext(start, stop, (a, b))
        # print('end')
        rotate_2D_matrix(start + 1, stop - 1)
    rotate_2D_matrix(0, len(matrix))
