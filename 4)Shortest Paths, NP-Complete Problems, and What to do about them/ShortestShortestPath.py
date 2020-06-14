from math import inf


def extractGraph(file):
    n, m = map(int, file.readline().split())
    G = {}

    for _ in range(m):
        i, j, weight = map(int, file.readline().split())
        i, j = i-1, j-1
        if i in G:
            G[i][j] = weight
        else:
            G[i] = {j: weight}

    return G, n, m


def FloydWarshal(G, n):
    # initialise A
    A = [[[inf]*2 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j][0] = 0
            elif i in G and j in G[i]:
                A[i][j][0] = G[i][j]

    # The Alg
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j][1] = min(A[i][j][0], A[i][k][0]+A[k][j][0])

        # copy A[i][j][1] to A[i][j][0]
        for i in range(n):
            for j in range(n):
                A[i][j][0] = A[i][j][1]

    # check for -ve cycle
    for i in range(n):
        if A[i][i][1] < 0:
            return None

    # get the Shortest Shortest Path
    return min(A[i][j][1] for j in range(n) for i in range(n))


if __name__ == '__main__':
    for fileName in ('g1.txt', 'g2.txt', 'g3.txt'):
        file = open(fileName)
        G, n, m = extractGraph(file)
        shortestShortestPath = FloydWarshal(G, n)
        print(shortestShortestPath)
        file.close()
