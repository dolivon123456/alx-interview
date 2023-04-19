#!/usr/bin/python3
"""return list of pascal triangle numbers"""


def pascal_triangle(n: int) -> list:
    """
        return a list of numbers representing pascal triangle
        param: n - size of triangle
    """

    iList = []
    for i in range(n):
        iList.append([])
        iList[i].append(1)

        for j in range(1, i):
            iList[i].append(iList[i-1][j-1]+iList[i-1][j])
        if i == 0:
            continue
        iList[i].append(1)
    return iList
