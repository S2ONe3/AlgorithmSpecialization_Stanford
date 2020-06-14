# FAIL!!!

def printSizes(sizes):
    sizes.sort(reverse=True)
    for i in sizes:
        print(i, end=',')


def reverseGraph(graph):
    pass


def DFS(graph, node):
    pass


def DFS_Loop(graph, sizes = None):
    global t
    t = 0
    global s
    s = None



def computeSccSizes(graph, sizes):
    rev_graph = reverseGraph(graph)
    DFS_Loop(rev_graph)
    sizes = DFS_Loop(graph)


if __name__ == '__main__':
    f = open("SCC.txt", 'r')
    Graph = [[0 for _ in range(875714)] for _ in range(875714)]
    for x in f:
        (a, b) = map(int, x.split())
        Graph[a-1][b-1] = 1;
    sizes = []
    computeSccSizes(Graph, sizes)
    printSizes(sizes)
