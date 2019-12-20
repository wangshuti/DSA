# BFS and DFS
## Graph
要理解BFS和DFS，首先要了解graph的概念                          
>圖(graph)是由節點(node)和邊(edge)組合而成的非線性結構，如果我們想要從其中的一個節點開始，走訪到其有直接或是間接連接的其它所有節點,可以依靠深度優先搜尋法(DFS, Depth-first Search)或是廣度優先搜尋法(BFS, Breadth-first Search)來達成。                       
[graph的補充說明](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)          

## BFS-廣度優先搜尋
### Definition
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.              
         
>It uses the opposite strategy as depth-first search, which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.                                       

>The Q queue contains the frontier along which the algorithm is currently searching.               
Nodes can be labelled as discovered by storing them in a set, or by an attribute on each node, depending on the implementation.                       
>Note that the word node is usually interchangeable with the word vertex.            

>The parent attribute of each node is useful for accessing the nodes in a shortest path, for example by backtracking from the destination node up to the starting node, once the BFS has been run, and the predecessors nodes have been set.           
                 
广度优先搜索在进一步遍历图中顶点之前，先访问当前顶点的所有邻接结点。                 
a .首先选择一个顶点作为起始结点，并将其染成灰色，其余结点为白色。           
b. 将起始结点放入队列中。          
c. 从队列首部选出一个顶点，并找出所有与之邻接的结点，将找到的邻接结点放入队列尾部，将已访问过结点涂成黑色，没访问过的结点是白色。如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现          
d. 按照同样的方法处理队列中的下一个结点。          
           
### 時間與複雜度           
時間複雜度可以表示為**O(|V|+|E|)** ，因為在最壞的情況下都會探索每個頂點和每個邊緣。|V|是頂點的數量，|E|是圖中的邊數。注意O(|E|)可能會有所不同O(1)和 O(|V|^2)，具體取決於輸入圖的稀疏程度。         
           
如果提前知道圖中的頂點數量，並且使用其他數據結構來確定哪些頂點已經添加到隊列中，則空間複雜度可以表示為 O(|V|)，在哪裡|V|是一組頂點的基數。這是圖形本身所需的空間的補充，該空間可能根據算法實現所使用的圖形表示而有所不同。       
            
當使用太大而無法顯式存儲（或無限存儲）的圖時，用不同的術語來描述廣度優先搜索的複雜性更為實用：找到距起始節點d的節點（以數量為單位） BFS佔用O(bd +1)時間和內存，其中b是圖形的“ 分支因子 ”（平均出度）。        
          
### 流程圖         
基本就是出队的顶点变成黑色，在队列里的是灰色，还没入队的是白色。        
                          
![image](https://github.com/wangshuti/DSA/blob/master/week12/image/BFS1.JPG)         
初始状态，从顶点1开始，队列={1}              
![image](https://github.com/wangshuti/DSA/blob/master/week12/image/BFS2.JPG)         
访问1的邻接顶点，1出队变黑，2,3入队，队列={2,3,}             
![image](https://github.com/wangshuti/DSA/blob/master/week12/image/BFS3.JPG)   
访问2的邻接结点，2出队，4入队，队列={3,4}             
![image](https://github.com/wangshuti/DSA/blob/master/week12/image/BFS4.JPG)   
访问3的邻接结点，3出队，队列={4}          
![image](https://github.com/wangshuti/DSA/blob/master/week12/image/BFS5.JPG)         
访问4的邻接结点，4出队，队列={ 空}, 结点5对于1来说不可达。         
           
### Code        
```Python
    def BFS(self, s):
        search_queue = deque()
        search_queue += self.graph[s]

        path = []          #建立path以記錄待訪尋的頂點
        searched = []      #建立searched以記錄已訪尋的頂點

        path.append(s)     #將起始頂點加入path
        searched.append(s) #將起始點加入searched

        while search_queue:
            current_node = search_queue.popleft()           #current node =依照queue先進先出的特性移除的第一個元素
            if not current_node in searched:                #如果目前的node不在searched裡面
                path.append(current_node)                   #將current node加入path
                searched.append(current_node)               #也加入searched
                search_queue += self.graph[current_node]
        return path
```           
            
## DFS-深度優先搜尋          
### Definiton
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.          
               
>The time and space analysis of DFS differs according to its application area. In theoretical computer science, DFS is typically used to traverse an entire graph, and takes time O(|V|+|E|),linear in the size of the graph. In these applications it also uses space O(|V|) in the worst case to store the stack of vertices on the current search path as well as the set of already-visited vertices.          
       
>Thus, in this setting, the time and space bounds are the same as for breadth-first search and the choice of which of these two algorithms to use depends less on their complexity and more on the different properties of the vertex orderings the two algorithms produce.
             
深度优先搜索在搜索过程中访问某个顶点后，需要递归地访问此顶点的所有未访问过的相邻顶点。          
初始条件下所有节点为白色，选择一个作为起始顶点，按照如下步骤遍历：           
a. 选择起始顶点涂成灰色，表示还未访问           
b. 从该顶点的邻接顶点中选择一个，继续这个过程（即再寻找邻接结点的邻接结点），一直深入下去，直到一个顶点没有邻接结点了，涂黑它，表示访问过了       
c. 回溯到这个涂黑顶点的上一层顶点，再找这个上一层顶点的其余邻接结点，继续如上操作，如果所有邻接结点往下都访问过了，就把自己涂黑，再回溯到更上一层。      
d. 上一层继续做如上操作，知道所有顶点都访问过。         
             
### 流程圖
从顶点1开始做深度搜索：
初始状态，从顶点1开始           
![image](https://github.com/wangshuti/DSA/blob/master/week13/image/DFS1.JPG)          
依次访问过顶点1,2,3后，终止于顶点3         
![image](https://github.com/wangshuti/DSA/blob/master/week13/image/DFS2.JPG)                   
从顶点3回溯到顶点2，继续访问顶点5，并且终止于顶点5        
![image](https://github.com/wangshuti/DSA/blob/master/week13/image/DFS3.JPG)          
从顶点5回溯到顶点2，并且终止于顶点2         
![image](https://github.com/wangshuti/DSA/blob/master/week13/image/DFS4.JPG)           
从顶点2回溯到顶点1，并终止于顶点1         
![image](https://github.com/wangshuti/DSA/blob/master/week13/image/DFS5.JPG)          
从顶点4开始访问，并终止于顶点4                    
               
### Code         
```Python
    def DFS(self, s):
        search_stack = deque()
        search_stack += self.graph[s]

        path = []           #建立path以記錄待訪尋的頂點
        searched = []       #建立searched以記錄待訪尋的頂點

        path.append(s)      #將起始頂點加入path
        searched.append(s)  #將起始頂點加入searched

        while search_stack:
            current_node = search_stack.pop()        #current node =依照queue先進先出的特性移除的第一個元素
            if not current_node in searched:         #如果目前的node不在searched裡面
                path.append(current_node)            #將current node加入path
                searched.append(current_node)        #也加入searched
                search_stack += self.graph[current_node]
        return path
```
           
## BFS vs. DFS
1.在DFS中，使用**佇列**儲存節點，而在BFS中，使用**棧**儲存節點。原因就在於二者優先次序的不同。        
>佇列是一種先進先出的資料結構，對於每一個節點而言，每一次搜尋，都是優先這一個節點的子節點，所以每一次加入等待序列之後，都要等到某一個節點的所有子節點都被訪問完畢， 才可以進行下一個節點的訪問，這正好是，先進入等待序列 的節點，先出序列進行計算，而後進入的，則後出，所以使用佇列儲存。           
               
>棧是一種先進後出的資料結構，在DFS中，我們要對每一條路徑走到底，才可以回溯前驅節點，所以當節點加入等待序列之後，都要先讓後加入的（也就是子節點中的某一個） 節點先進行運算， 以保證是一條路走到底，所以符合棧的設計。        
                      
2.在搜尋的執行方式上，BFS和DFS也存在差異                
>BFS像是，一个人迷路，但是他有技能（分身术）它遇到分叉路口，不是选一个走，而是分身多个人都试试，比如有A、B、C三个分叉路口，它A路走一步，紧接着B路也走一步，然后C路也赶紧走一步，步伐整齐统一，直到所有的路走过了。            
            
>DFS則是，一个人迷路，遇到很多分叉路口，他只有一个人，并且想走出去，所以只能一个个尝试，一条道路走到黑，发现到头了，然后再拐回去走刚才这条路的其他分叉路口，最后发现这条路的所有分叉路口走完了，选择另外一条路继续以上操作，直到所有的路都走过了。            
            
3.所使用的記憶體容量
>BFS is going to use more memory depending on the branching factor... however, BFS is a complete algorithm... meaning if you are using it to search for something in the lowest depth possible, BFS will give you the optimal solution. BFS space complexity is  O(b^d) ... the branching factor raised to the depth (can be A LOT of memory).        
             
>DFS on the other hand, is much better about space however it may find a suboptimal solution. Meaning, if you are just searching for a path from one vertex to another, you may find the suboptimal solution (and stop there) before you find the real shortest path. DFS space complexity is  O(|V|) ... meaning that the most memory it can take up is the longest possible path.                   
                
4. According to tree, they depends on the structure of the search tree          
>1.If you know a solution is not far from the root of the tree, a breadth first search (BFS) might be better.            
2.If the tree is very deep and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.     
3.If the tree is very wide, a BFS might need too much memory, so it might be completely impractical.          
4.If solutions are frequent but located deep in the tree, BFS could be impractical.         
5.If the search tree is very deep you will need to restrict the search depth for depth first search (DFS), anyway (for example with iterative deepening).          
           
## References
http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html             
https://en.wikipedia.org/wiki/Breadth-first_search                    
https://en.wikipedia.org/wiki/Depth-first_search           
https://www.jianshu.com/p/70952b51f0c8           
https://www.zhihu.com/question/28549888/answer/41231930           
https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf          
