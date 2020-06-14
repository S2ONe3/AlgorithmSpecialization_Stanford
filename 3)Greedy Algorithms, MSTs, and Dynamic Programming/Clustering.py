# Clustering 1
from networkx.utils.union_find import UnionFind
import heapq

with open('clustering1.txt') as file:
    k = 4
    n = int(file.readline())
    E = []
    while file:
        try:
            p, q, weight = map(int, file.readline().split())
            p -=1; q-=1
            heapq.heappush(E, (weight, {p, q}))
        except ValueError:
            break;

uFind = UnionFind(range(n))
while len({uFind[v] for v in range(n)}) > k:
    weight, (p, q) = heapq.heappop(E)
    uFind.union(p, q)

while uFind[p] == uFind[q]:
    weight, (p, q) = heapq.heappop(E)

print(weight)


# -------------------------------------------------------------------------------------------------------------------- #
# Big Clustering

from networkx.utils.union_find import UnionFind


if __name__ == '__main__':
    with open("clustering_big.txt") as file:
        n, nBits = map(int, file.readline().split())

        V = {}
        for i in range(n):
            key = int(file.readline().replace(' ', ''), 2)
            try:
                V[key].append(i)
            except KeyError:
                V[key] = [i]

    uFind = UnionFind(range(n))

    Masks = [0] + sorted(list({(1 << i) | (1 << j) for i in range(nBits) for j in range(nBits)}))


    for mask in Masks:
        for v in V:
            if (v ^ mask) in V.keys():
                uFind.union(v^mask, v)

    pointer_set = {uFind[v] for v in V}
    print(len(pointer_set))

