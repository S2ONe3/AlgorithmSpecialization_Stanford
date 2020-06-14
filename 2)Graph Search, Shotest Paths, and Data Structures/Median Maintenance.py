import heapq
import heapq_max

if __name__ == '__main__':
    f = open('Median.txt')
    #f = open('Test.txt')
    medians = []
    Hhi = []
    Hlo = []

    for x in f:
        i = int(x)
        if len(Hhi) == 0:
            heapq_max.heappush_max(Hlo, i)
        elif i > Hlo[0]:
            heapq.heappush(Hhi, i)
        else:
            heapq_max.heappush_max(Hlo, i)

        if len(Hhi) > len(Hlo) + 1:
            heapq_max.heappush_max(Hlo, heapq.heappop(Hhi))
        elif len(Hlo) > len(Hhi) + 1:
            heapq.heappush(Hhi, heapq_max.heappop_max(Hlo))

        if len(Hlo) < len(Hhi):
            medians.append(Hhi[0])
        else:
            medians.append(Hlo[0])

    print(medians)
    print(sum(medians)%10000)