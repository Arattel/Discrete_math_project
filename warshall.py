import doctest
from conjunction import *
def warshall(matrix):
    '''(list)->list
    This function applies warshall algorythm and find transitive ratio
    >>> warshall([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
    [[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
    '''
    k = len(matrix[0])
    for i in range(k):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                matrix[j] = disjunction_raw(matrix[j],matrix[i])
    return matrix
