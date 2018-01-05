import doctest
import itertools
import copy
from warshall import *
from math import sqrt


def split_into_matrix(binary):
    """(tuple)->list(list)
    This function makes square matrix from binary tuple.
    >>> split_into_matrix((0, 0, 0, 1))
    [[0, 0], [0, 1]]
    >>> split_into_matrix((0, 1, 0, 1))
    [[0, 1], [0, 1]]

    """
    matrix = []
    period = int(sqrt(len(binary)))
    for i in range(period):
        temp = list(binary[i * period: (i + 1) * period])
        matrix.append(temp)
    return matrix


def generate_matrix(size):
    """(int) -> list(list(list))
    This function generates all possible square matrix with given side.

    >>> generate_matrix(2) #doctest: +NORMALIZE_WHITESPACE
    [[[0, 0], [0, 0]], [[0, 0], [0, 1]],
    [[0, 0], [1, 0]], [[0, 0], [1, 1]],
    [[0, 1], [0, 0]], [[0, 1], [0, 1]],
    [[0, 1], [1, 0]], [[0, 1], [1, 1]],
    [[1, 0], [0, 0]], [[1, 0], [0, 1]],
    [[1, 0], [1, 0]], [[1, 0], [1, 1]],
    [[1, 1], [0, 0]], [[1, 1], [0, 1]],
    [[1, 1], [1, 0]], [[1, 1], [1, 1]]]

    """
    matrix = []
    binary = list(itertools.product([0, 1], repeat=size ** 2))
    for i in binary:
        matrix.append(split_into_matrix(i))
    return matrix


def is_transitive(matrix):
    """(list)->bool
    This function returns True if matrix ratio is transitive, else it returns
    False.

    >>> is_transitive([[1, 1], [1, 1]])
    True
    >>> is_transitive([[0, 1], [1, 0]])
    False

    """
    matrix1 = copy.deepcopy(matrix)
    if matrix == warshall(matrix1):
        return True
    else:
        return False


def number_of_transitive(n):
    """(int)->(int, list(list))
    This function inputs size of matrix and outputs number of possible
    transitive matrix with that size and all possible transitive matrix of that
    size.

    >>> number_of_transitive(2) #doctest: +NORMALIZE_WHITESPACE
    (13, [[[0, 0], [0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]],
    [[0, 0], [1, 1]], [[0, 1], [0, 0]], [[0, 1], [0, 1]], [[1, 0], [0, 0]],
    [[1, 0], [0, 1]], [[1, 0], [1, 0]], [[1, 0], [1, 1]], [[1, 1], [0, 0]],
    [[1, 1], [0, 1]], [[1, 1], [1, 1]]])

    """
    transitive = 0
    variants = generate_matrix(n)
    transitive_matrix = []
    for i in variants:
        if is_transitive(i):
            transitive += 1
            transitive_matrix.append(i)
    return (transitive, transitive_matrix)


n = int(input('Please, enter number of elements in set(from 1 to 4):  '))
print(number_of_transitive(n)[0])

doctest.testmod()
