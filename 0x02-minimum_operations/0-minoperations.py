#!/usr/bin/python3

"""
This module provides the function `minOpertions`
"""


def minOperations(n):
    """
    This is a function that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    """
    if n < 1 or type(n) != int:
        # Checks if the input is not a positive integer
        return 0
    operations = 0 # number of operations counter
    while n >= 2:
        # number of H characters from all operations cannot be less than 2
        lowestFactor = 2 # initialized at 2 which is 
        # the lowest possible factor asides 1
        while lowestFactor < n + 1:
            # loops to find the lowest factor of n
            if n % lowestFactor == 0:
                # when the lowest factor is found it's the number of operations
                # performed to arrive at the current n number of H characters
                # i.e 1 `copyAll`, lowestFactor - 1 `paste`
                operations += lowestFactor # increment the number of operations
                n /= lowestFactor # divide the current n by lowestFactor to
                # get the result of all operations prior
                break # repeat the whole process
            lowestFactor += 1 # increments to keep searching for the lowest factor
    return operations # returns the minimum number of operations
