for filename in ('knapsack1.txt', 'knapsack_big.txt'):
    with open(filename) as file:
        W, n = map(int, file.readline().split())
        A = [[0 for x in range(W+1)] for i in range(2)]

        for i in range(n):
            v_i, w_i = map(int, file.readline().split())
            for x in range(W+1):
                if w_i > x:
                    A[1][x] = A[0][x]
                else:
                    A[1][x] = max(A[0][x], A[0][x-w_i] + v_i)
            A[0] = A[1][:]
        print(A[1][W])