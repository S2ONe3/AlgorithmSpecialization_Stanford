with open('mwis.txt') as file:
    n = int(file.readline())
    w = [0, int(file.readline())]
    A = [0, w[1]]

    for i in range(2, n+1):
        w.append(int(file.readline()))
        A.append(max(A[i-1], A[i-2]+w[i]))

Check = A[:]
i = n
while i >= 1:
    if A[i-1] >= A[i-2]+w[i]:
        Check[i] = False
        i-=1
    else:
        Check[i] = True
        Check[i-1] = False
        i-=2
print(Check[1], Check[2], Check[3], Check[4], Check[17], Check[117], Check[517], Check[997])
