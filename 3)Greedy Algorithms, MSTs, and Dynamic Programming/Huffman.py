import heapq
from sys import setrecursionlimit
setrecursionlimit(1500)


class BST:
    class Node:
        def __lt__(self, other):
            return True if self.weight < other.weight else False

        def __eq__(self, other):
            if isinstance(other, Node):
                return True if self.name == other.name else False
            return True if self.name == other else False

        def __str__(self):
            return str(self.name)

    class numNode(Node):
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight
            self.minDeapth = 0
            self.maxDeapth = 0

    class conNode(Node):
        def __init__(self, NodeA, NodeB):
            self.Node0 = NodeA
            self.Node1 = NodeB
            self.name = (NodeA.name, NodeB.name)
            self.weight = NodeA.weight + NodeB.weight
            self.minDeapth = min(self.Node0.minDeapth, self.Node1.minDeapth) + 1
            self.maxDeapth = max(self.Node0.maxDeapth, self.Node1.maxDeapth) + 1


    def __init__(self, a, b):
        if isinstance(a, BST.Node):
            self.root = BST.conNode(a, b)
        else:
            self.root = BST.numNode(a, b)


    def join(self, other):
        return BST(self.root, other.root)


    def minDeapth(self):
        return self.root.minDeapth
    def maxDeapth(self):
        return self.root.maxDeapth

    def __lt__(self, other):
        return True if self.root < other.root else False

    def __str__(self):
        return str(self.root)






def Huffman(Sigma):
    if len(Sigma) <= 2:
        T = Sigma[0].join(Sigma[1])
        return T

    a = heapq.heappop(Sigma)
    b = heapq.heappop(Sigma)
    ab = a.join(b)
    heapq.heappush(Sigma, ab)

    return Huffman(Sigma)




with open('huffman.txt') as file:
    Sigma = []
    for i in range(int(file.readline())):
        Sigma.append(BST(i, int(file.readline())))
heapq.heapify(Sigma)
T = Huffman(Sigma)
print(T)
print(T.minDeapth(), T.maxDeapth())