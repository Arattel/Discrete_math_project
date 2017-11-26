import doctest
def disjunction(matrix1,matrix2):
    '''(list,list)->list
    This function input 2 matrix and returns their disjuction
    >>> disjunction([[0,1,0],[1,1,1],[1,0,0]],[[0,1,0],[0,1,1],[1,1,1]])
    [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    '''
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Матриці різного розміру, неможливо обрахувати диз'юнкцію")
        return None
    else:
        m = len(matrix1)
        n = len(matrix1[0])
        disjunct = matrix1
        for i in range(m):
            for j in range(n):
                if matrix1[i][j] or matrix2[i][j]:
                    disjunct[i][j] = 1
                else:
                    disjunct[i][j] = 0
        return disjunct
def conjunction(matrix1,matrix2):
    '''(list,list)->list
    This function input 2 matrix and returns their conjuction
    >>> conjunction([[0,1,0],[1,1,1],[1,0,0]],[[0,1,0],[0,1,1],[1,1,1]])
    [[0, 1, 0], [0, 1, 1], [1, 0, 0]]
    '''
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Матриці різного розміру, неможливо обрахувати кон'юнкцію")
        return None
    else:
        m = len(matrix1)
        n = len(matrix1[0])
        conjunct = matrix1
        for i in range(m):
            for j in range(n):
                if matrix1[i][j] and matrix2[i][j]:
                    conjunct[i][j] = 1
                else:
                    conjunct[i][j] = 0
        return conjunct
def disjunction_raw(raw1,raw2):
    '''(list,list)->list
    This function input 2 matrix and returns their disjuction
    >>> disjunction_raw([0,1,0],[1,1,1])
    [1, 1, 1]
    '''
    if len(raw1) != len(raw2):
        print("Матриці різного розміру, неможливо обрахувати диз'юнкцію")
        return None
    else:
        m = len(raw1)
        disjunct = raw1
        for i in range(m):
                if raw1[i] or raw2[i]:
                    disjunct[i] = 1
                else:
                    disjunct[i] = 0
        return disjunct
doctest.testmod()
