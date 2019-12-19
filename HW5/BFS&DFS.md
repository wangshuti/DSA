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
                          
![image](https://github.com/wangshuti/DSA/blob/master/week12/BFS1.JPG)         
初始状态，从顶点1开始，队列={1}              
![image](https://github.com/wangshuti/DSA/blob/master/week12/BFS2.JPG)         
访问1的邻接顶点，1出队变黑，2,3入队，队列={2,3,}             
![image](https://github.com/wangshuti/DSA/blob/master/week12/BFS3.JPG)   
访问2的邻接结点，2出队，4入队，队列={3,4}             
![image](https://github.com/wangshuti/DSA/blob/master/week12/BFS4.JPG)   
访问3的邻接结点，3出队，队列={4}          
![image](https://github.com/wangshuti/DSA/blob/master/week12/BFS5.JPG)         
访问4的邻接结点，4出队，队列={ 空}, 结点5对于1来说不可达。         
           
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
![image](https://github.com/wangshuti/DSA/blob/master/week12/DFS1.JPG)
依次访问过顶点1,2,3后，终止于顶点3         
![image](https://github.com/wangshuti/DSA/blob/master/week12/DFS2.JPG)
从顶点3回溯到顶点2，继续访问顶点5，并且终止于顶点5        
![image](https://github.com/wangshuti/DSA/blob/master/week12/DFS3.JPG)
从顶点5回溯到顶点2，并且终止于顶点2         
![image](https://github.com/wangshuti/DSA/blob/master/week12/DFS4.JPG)
从顶点2回溯到顶点1，并终止于顶点1         
![image](https://github.com/wangshuti/DSA/blob/master/week12/DFS5.JPG)
从顶点4开始访问，并终止于顶点4                           
            
## BFS vs. DFS
This non-recursive implementation is similar to the non-recursive implementation of depth-first search, but differs from it in two ways:
           
>1.it uses a **queue (First In First Out)** instead of a **stack** and          
2.it checks whether a vertex has been discovered before enqueueing the vertex rather than delaying this check until the vertex is dequeued from the queue.       
          
## References
http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html       
https://en.wikipedia.org/wiki/Breadth-first_search           
https://en.wikipedia.org/wiki/Depth-first_search
https://www.jianshu.com/p/70952b51f0c8 
