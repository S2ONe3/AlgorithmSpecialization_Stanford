def extractMinEdge(Graph):
    minedge = (None, None)
    minLength = 1000000
    for v in Graph:
        for w in Graph[v][-1].keys():
            if (Graph[v][0] is True) and (Graph[w][0] is False):
                if Graph[v][1] + Graph[v][-1][w] < minLength:
                    minLength = Graph[v][1] + Graph[v][-1][w]
                    minedge = (v,w)

    return minedge

def DijkstraSPLength(Graph):
    Graph[1][0] = True  #Explored
    Graph[1][1] = 0     #SP = 0  <= Starting Point
    for _ in range(len(Graph)):
        (vStar,wStar) = extractMinEdge(Graph)
        if vStar == None:
            return
        Graph[wStar][0] = True
        Graph[wStar][1] = Graph[vStar][1] + Graph[vStar][-1][wStar]


if __name__ == "__main__":
    f = open("dijkstraData.txt", 'r')
    #f = open("Test.txt", 'r')
    Graph = {}
    for x in f:
        Graph[int(x.split()[0])] = [False, 1000000, {}]   #Explored, SP, Edges
        for edge in x.split()[1:]:
            Graph[int(x.split()[0])][-1][int(edge.split(',')[0])] = int(edge.split(',')[1])

    print(Graph)

    DijkstraSPLength(Graph)

    ans = [Graph[i][1] for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]
    print(ans)
