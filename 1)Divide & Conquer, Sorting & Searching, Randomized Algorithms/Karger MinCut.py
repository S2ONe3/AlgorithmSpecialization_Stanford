
from random import sample

def KMinCutCount(G):
    while len(G) >2:
        #select a random Edge
        randV = sample(G.keys(),1)[0]
        randU = sample(G[randV],1)[0]

        #merge v & u into 1 Vertex
        G[randV] += G[randU]
        G.pop(randU)
        #remove self loops
        while randU in G[randV] or randV in G[randV]:
            G[randV].remove(randV)
            G[randV].remove(randU)
        for V in G:
            while randU in G[V]:
                G[V].remove(randU)
                G[V].append(randV)

    randV = sample(G.keys(),1)[0]
    return len(G[randV])


if __name__ == '__main__':
    f = open('kargerMinCut.txt', 'r')
    G = {int(x.split()[0]):list(map(int,x.split()[1:])) for x in f}

    counts = []
    for i in range(len(G)**2):
        counts.append(KMinCutCount(G))

    print(min(counts))