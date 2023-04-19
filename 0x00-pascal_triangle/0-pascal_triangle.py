#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      The integers representing the Pascal’s triangle
    '''
    triangle = []
    if n == 0:
        return triangle
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        if (i > 0):
            for j in range(1, i):
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle[i].append(1)
    return triangle
