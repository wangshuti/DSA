# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict

#Class to represent a graph
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    def addEdge(self,u,v,w):
        """
        :type u,v,w: int
        :rtype: None
        """
        self.graph.append([u,v,w])

    def Dijkstra(self, s):
        """
        :type s: int
        :rtype: dict
        """
        visited = []
        distance = {s: 0}
        node = list(range(self.V))
        if s in node:
            node.remove(s)
            visited.append(s)
        else:
            return None

        for i in node:
            distance[i] = self.graph[s][i]
        prefer = s
        while node:
            _distance = float('inf')
            for i in visited:
                for j in node:
                    if self.graph[i][j] > 0:
                        if _distance > distance[i] + self.graph[i][j]:
                            _distance = distance[j] = distance[i] + self.graph[i][j]
                            prefer = j
            visited.append(prefer)
            node.remove(prefer)

        ret = {}
        for i in range(self.V):
            ret[str(i)] = distance[i]
        return ret

    def find(self, x, pres):
        root, p = x, x
        while root != pres[root]:
            root = pres[root]

        while p != pres[p]:
            p, pres[p] = pres[p], root
        return root

    def join(self, x, y, pres, ranks):
        h1, h2 = self.find(x, pres), self.find(y, pres)
        if h1 != h2:
            if ranks[h1] < ranks[h2]:
                pres[h1] = h2
            else:
                pres[h2] = h1
                if ranks[h1] == ranks[h2]:
                    ranks[h1] += 1

    def Kruskal(self):
        """
        :rtype: dict
        """
        n = self.V
        pres, ranks = [e for e in range(n)], [0] * n
        edges = sorted(self.graph, key=lambda x: x[-1])
        mst_edges, num = [], 0
        for edge in edges:
            if self.find(edge[0], pres) != self.find(edge[1], pres):
                mst_edges.append(edge)
                self.join(edge[0], edge[1], pres, ranks)
                num += 1
            else:
                continue
            if num == n:
                break
        ret = {}
        for [u, v, w] in mst_edges:
            ret[str(u)+'-'+str(v)] = w
        return ret
