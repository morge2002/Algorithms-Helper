import math
from copy import deepcopy

from tabulate import tabulate


def matrixMult(W):
    def matMul(A, B):
        n = len(A)
        C = [[[0, 0] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j][0] = math.inf
                if i == j:
                    C[i][j] = [0, 0]
                for k in range(n):
                    # print(i, k, k, j)
                    newCost = A[i][k][0] + B[k][j][0]
                    if newCost < C[i][j][0]:
                        # print(i, j, k)
                        C[i][j][0] = newCost
                        C[i][j][1] = k + 1
        return C

    # returns table W with entries [shortest path length, intermediary node (0 is direct edge)]
    n = len(W)
    E = [[[x, 0] for x in y] for y in W]
    W = deepcopy(E)

    iter = 1
    while iter != n - 1:
        if 2 * iter < n:
            W = matMul(W, W)
            iter *= 2
        else:
            W = matMul(W, E)
            iter += 1
        # print(iter, tabulate(W))
    return W


# EXAMPLE =====================
i = math.inf
W = [[0, 5, 3, i, i, i],
     [i, 0, i, 5, i, i],
     [i, 4, 0, i, 3, i],
     [i, 8, i, 0, -5, 12],
     [i, 7, -2, i, 0, -1],
     [i, i, i, i, 8, 0]]
res = matrixMult(W)
print("MATRIX MULTIPLICATION")
print(tabulate(res))
print()
