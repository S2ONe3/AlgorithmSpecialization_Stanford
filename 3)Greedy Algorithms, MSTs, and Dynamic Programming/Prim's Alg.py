from math import inf
class Graph:
    def __init__(self, file):
        self.n, self.m = map(int,file.readline().split())
        self.E = [(int(x.split()[2]), {int(x.split()[0]), int(x.split()[1])}) for x in file]

    def findMin(self):
        min = (inf, None)
        for edge in self.E:
            a, b = list(edge[1])
            if (a in self.X and b not in self.X) or (a not in self.X and b in self.X):
                if edge < min:
                    min = edge
                    if a not in self.X:
                        v = a
                    else:
                        v = b
        return (min[0], v)

    def calcCost(self):
        self.X = {1}
        sumT =0
        while len(self.X) < self.n:
            eVal,v = self.findMin()
            self.X.add(v)
            sumT += eVal

        return sumT




if __name__ == '__main__':
    G = Graph(open('edges.txt'))
    print(G.calcCost())