# Kruskal<br>
是minimum spanning tree的運用<br>
## 生成樹<br>             
（1）定義：所有頂點均由邊連線在一起，但不存在迴路的圖叫該圖的生成樹<br>
（2）深度優先生成樹與廣度優先生成樹<br>
（3）一個圖可以有許多棵不同的生成樹，所有生成樹具有以下共同特點：<br>
>生成樹的頂點個數與圖的頂點個數相同<br>
生成樹是圖的極小連通子圖<br>          
## 最小生成樹<br>    
生成樹的每條邊上的權值之和最小。<br>
## Definiton<br>
設連通網N=(V,{E})，令最小生成樹<br>
（1）初始狀態為只有n個頂點而無邊的非連通圖T=(V,{NULL})，每個頂點自成一個連通分量<br>
（2）在E中選取代價最小的邊，若該邊依附的頂點落在T中不同的連通分量上，則將此邊加入到T中；否則，捨去此邊，選取下一條代價最小的邊<br>
（3）依此類推，直至T中所有頂點都在同一連通分量上為止<br>
## 時間複雜度<br>
一、排序圖上所有邊。 O(ElogE) 。<br>
二、連結 MSS ，採用「 Disjoint-set Forest 」。 O(Eα(E,V)) 。<br>
總時間複雜度為 O(ElogE) 。<br>
如果兩點之間有多條邊，預先以 Graph Traversal 掃描一次所有邊，保留權重最小的邊，仍可求得正確答案。兩點之間只剩下一條邊，邊的總數至多 C{V,2} = V(V-1)/2 條。時間複雜度 O(ElogE) 可以改寫成 O(ElogV²) = O(2ElogV) = O(ElogV) 。<br>
<br>
## 流程圖<br>
![image](https://github.com/wangshuti/DSA/blob/master/week14/image/k1.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week14/image/k2.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week14/image/k3.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week14/image/k4.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week14/image/k5.JPG)<br>
# Dijkstra<br>
是shortest path的運用<br>
## Path<br>
在圖上任取兩點，分別作為起點和終點，我們可以規劃許多條由起點到終點的路線。不會來來回回繞圈子、不會重覆經過同一個點和同一條邊的路線，就是一條「路徑」。<br>
如果起點到終點是不通的，那麼就不存在起點到終點的路徑。如果起點和終點一樣，那麼就存在路徑，路徑是一個點、零條邊。<br>
路徑也有權重。路徑經過的每一條邊，沿路加總權重，就是路徑的權重（通常只加總邊的權重，而不考慮點的權重）。路徑的權重，可以想像成路徑的總長度。<br>
<br>
## Shortest path<br>
是由起點到終點、權重最小的路徑，可能有許多條，也可能不存在。起點到終點不通、不存在路徑的時候，就沒有最短路徑。<br>
「最短路徑」不見得是邊最少、點最少的路徑。<br>
<br>
## Shortest path-tree<br>
最短路徑有一個特別的性質：每一條最短路徑，都是由其它的最短路徑延展而得。一條最短路徑，截去末端之後，還是最短路徑。<br>
提到延展，就聯想到樹！引入延展的概念，最短路徑們得以形成一棵樹。<br>
在圖上選定一個起點，由起點到圖上各點的最短路徑們，形成一棵有向樹，稱作「最短路徑樹」。由於兩點之間的最短路徑不見得只有一條，所以最短路徑樹也不見得只有一種。<br>
<br>
## Shortest path-graph<br>
在圖上選定一個起點和一個終點，由起點到終點的所有最短路徑們，形成一張有向圖，稱作「最短路徑圖」，只有唯一一種。
當圖上每一條邊的權重都是正數，最短路徑圖是有向無環圖（ Directed Acyclic Graph, DAG ）
<br>
## Definition<br>
（1）初使時令 S={V0},T={其餘頂點}，T中頂點對應的距離值<br>
（2）若存在<V0,Vi>，為<V0,Vi>弧上的權值<br>
（3）若不存在<V0,Vi>，為無窮<br>
（4）從T中選取一個其距離值為最小的頂點W，加入S<br>
（5）對T中頂點的距離值進行修改：若加進W作中間頂點，從V0到Vi的距離值比不加W的路徑要短，則修改此距離值<br>
（6）重複上述步驟，直到S中包含所有頂點，即S=V為止<br>
## 流程圖<br>
以上面的例子做說明 ( - 代表無限大 ; D[i]: 1至 i的距離 ; P[i]: 至 i的上一個結點）<br>
![image](https://github.com/wangshuti/DSA/blob/master/week15/image/d1.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week15/image/d2.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week15/image/d3.JPG)<br>
![image](https://github.com/wangshuti/DSA/blob/master/week15/image/d4.JPG)<br>
所以終端機1~終端機7的最短路徑花費為16<br>
路徑為 1 → 2 → 3 → 6 → 5 → 7 (back trace)<br>
# Reference
http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html<br>
http://www.csie.ntnu.edu.tw/~u91029/Path.html<br>
http://dreamisadream97.pixnet.net/blog/post/168577620-dijkstra%E6%BC%94%E7%AE%97%E6%B3%95
