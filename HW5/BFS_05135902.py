from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        search_queue = deque()
        search_queue += self.graph[s]

        path = []
        searched = []

        path.append(s)
        searched.append(s)

        while search_queue:
            current_node = search_queue.popleft()
            if not current_node in searched:
                path.append(current_node)
                searched.append(current_node)
                search_queue += self.graph[current_node]
        return path

    def DFS(self, s):
        search_stack = deque()
        search_stack += self.graph[s]

        path = []
        searched = []

        path.append(s)
        searched.append(s)

        while search_stack:
            current_node = search_stack.pop()
            if not current_node in searched:
                path.append(current_node)
                searched.append(current_node)
                search_stack += self.graph[current_node]
        return path

    def show(self):
        print(list(self.graph.items()))

#References（程式碼自創，僅參考概念）
#http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html
#https://en.wikipedia.org/wiki/Breadth-first_search
#https://en.wikipedia.org/wiki/Depth-first_search
#https://www.jianshu.com/p/70952b51f0c8
#https://www.zhihu.com/question/28549888/answer/41231930
#https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf
