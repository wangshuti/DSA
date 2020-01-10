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
