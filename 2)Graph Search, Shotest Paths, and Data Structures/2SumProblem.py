RANGE = 10000
#RANGE = 10


if __name__ == '__main__':
    f = open('2sum.txt')
    #f = open('Test.txt')
    HT = set()
    t = [False]*(2*RANGE+1)

    for x in f:
        HT.add(int(x))

    #print(HT)

    for a in HT:
        for ts in range(-RANGE, RANGE+1):
            if HT.issuperset({ts-a}) and (ts != 2*a):
                t[10-ts] = True

    #print(t)
    print(sum(t))