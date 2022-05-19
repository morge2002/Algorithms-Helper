
I = 999


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def matrix_chain_product(n, d):
    print('matrix_chain_product')
    M = []
    n += 1
    J = []
    for i in range(n):
        M.append([0 for _ in range(n)])
        J.append([0 for _ in range(n)])
    for b in range(1, n):
        for i in range(1, n - b):
            k = i + b
            m = d[i - 1] * d[k]
            M[i][k] = 100000000
            for j in range(i, k):
                N = M[i][j] + m * d[j] + M[j + 1][k]
                if min([M[i][k], N]) == N:
                    if J[i][k] != 0 and M[i][k] == N:
                        J[i][k] = str(J[i][k]) + ', ' + str(j)
                    else:
                        J[i][k] = j

                M[i][k] = min([M[i][k], N])
    print_matrix(M)
    print()
    print_matrix(J)


matrix_chain_product(5, [3, 2, 5, 2, 4, 3])


def floyd_warshall(G):
    nV = len(G[0])
    print('Floyd Warshall')
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    values = []
    for i in range(len(G)):
        row = []
        for j in range(len(G)):
            if G[i][j] != 'x':
                row.append(0)
            else:
                row.append(999)
        values.append(row)
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                x = distance[i][j]
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                if distance[i][j] != x:
                    values[i][j] = k + 1

    print_matrix(distance)
    print(" ")
    print_matrix(values)


example_weights = [[0, 5, 3, I, I, I],
                   [I, 0, I, 5, I, I],
                   [I, 4, 0, I, 3, I],
                   [I, 8, I, 0, -5, 12],
                   [I, 7, -2, I, 0, -1],
                   [I, I, I, I, 8, 0]]
floyd_warshall(example_weights)





def CYK(w, P):
    print('CYK')
    M = []
    J = []
    n = len(w)
    for i in range(n):
        M.append([0 for _ in range(n)])
        J.append([0 for _ in range(n)])
        for prod in P:
            if prod[1] == w[i]:
                if M[i][i] != 0:
                    M[i][i] += ', ' + prod[0]
                else:
                    M[i][i] = prod[0]
    for b in range(n):
        for i in range(n - b):
            k = i + b
            for j in range(i, k):
                for prod in P:
                    jValues = []
                    if len(prod[1]) == 2:
                        if prod[1][0] in str(M[i][j]) and prod[1][1] in str(M[j + 1][k]):
                            if M[i][k] != 0:
                                if str(j + 1) not in str(J[i][k]):
                                    # J[i][k] = str(J[i][k]) + ', ' + str(j + 1)
                                    jValues.append(j+1)
                                if prod[0] not in M[i][k]:
                                    M[i][k] += ', ' + prod[0]
                            else:
                                M[i][k] = prod[0]
                                # J[i][k] = j + 1
                                jValues.append(j + 1)
                    if len(jValues) > 0:
                        if type(J[i][k]) == str:
                            tmp = (', (' + str(jValues) + ')').replace('[', '')
                            tmp = tmp.replace(']', '')
                            J[i][k] += tmp
                        else:
                            tmp = ('(' + str(jValues) + ')').replace('[', '')
                            tmp = tmp.replace(']', '')
                            J[i][k] = tmp

    if 'S' not in M[0][-1]:
        print("REJECT")
    print_matrix(M)
    print()
    print_matrix(J)


productions = [['S', 'AB'], ['S', 'BC'],
               ['A', 'BA'], ['A', 'a'],
               ['B', 'CC'], ['B', 'b'],
               ['C', 'AB'], ['C', 'a']]

CYK(w='baaba', P=productions)

jProductions = [['S', 'AB'], ['S', 'CS'],
                ['A', 'AC'], ['A', 'a'],
                ['B', 'BC'], ['B', 'b'],
                ['C', 'a'], ['C', 'b']]

CYK('abab', jProductions)
