import timeit

pureMult = """
import numpy as np
def matrix_mult(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    if cols_a != rows_b:
        return

    C = [[0 for row in range(cols_b)] for col in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return C
matrix_a = np.random.random((200, 200))
matrix_b = np.random.random((200, 200))
res = matrix_mult(matrix_a, matrix_b)
"""

numPyMult = """
import numpy as np
matrix_a = np.random.random((200, 200))
matrix_b = np.random.random((200, 200))
res = np.dot(matrix_a, matrix_b)
"""

print("pure python:")
print(timeit.timeit(pureMult, number=1))
print("numpy:")
print(timeit.timeit(numPyMult, number=1))
