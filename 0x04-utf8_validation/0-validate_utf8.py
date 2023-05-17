#!/usr/bin/python3

"""
This module provides the function validUTF8(data)
"""


def convertToBinary(data):
    """
    This function converts a list of decimals to
    a list of utf-8 binaries
    """
    i = 0
    byte = data
    byte = bin(byte)[2:]
    if len(byte) < 8:
        byte = '0'*(8 - len(byte)) + byte
    return byte


def validUTF8(data):
    """
    This function validates a data set
    to represents a valid UTF-8 encoding
    """
    if data is None or len(data) == 0:
        return False
    if type(data) != list:
        return False
    if not isinstance(all(data), int):
        return False
    data = list(map(convertToBinary, data))
    i = 0
    while i < len(data):
        byte = data[i]
        if len(byte) > 8:
            return False
        if byte[0] == '0':
            i += 1
            continue
        numOfBytes = 0
        for j in range(len(byte)):
            if byte[j] == '0':
                numOfBytes = j
                if i + j > len(data):
                    return False
                for a in range(1, numOfBytes):
                    a += i
                    nextByte = data[a]
                    if nextByte[0] != '1' or nextByte[1] != '0':
                        return False
                i += j - 1
                break
        i += 1
    return True
