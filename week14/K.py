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
