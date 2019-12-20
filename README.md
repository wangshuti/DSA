# My DSA learning record
## 自我介紹~    
姓名：王舒荑    
學號：05135902    
系級：心理四  

## [week2](https://github.com/wangshuti/DSA/tree/master/week2)     
### Linkedlist           
Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點      
-[補充資料](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)        
      
[Linkedlist_707](https://github.com/wangshuti/DSA/blob/master/week2/Linkedlist_707.py)    
-leetcode no.707：上課所用的leetcode    
[Linkedlist_note](https://github.com/wangshuti/DSA/blob/master/week2/Linkedlist_note.py)   
-網絡搜尋之關於Linkedlist的解釋      
[Linkedlist_206](https://github.com/wangshuti/DSA/blob/master/week2/Linkedlist_206.py)    
-leetcode no.206：課後Leetcode練習：reverse of Linkedlist    

## [week3](https://github.com/wangshuti/DSA/tree/master/week3)     
### 1.stack       
Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。        
-[補充資料-以array與linkedlist實作](http://alrightchiu.github.io/SecondRound/stack-yi-arrayyu-linked-listshi-zuo.html)          
### 2.queue                
Queue(佇列)是一種概念性的抽象資料結構，可以分別使用Linked list(連結串列)與Array(陣列)來實作。           
-[補充資料-以linkedlist實作](http://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)       
-[補充資料-以array實作](http://alrightchiu.github.io/SecondRound/queue-yi-arrayshi-zuo-queue.html)      
      
[stack&queue_155](https://github.com/wangshuti/DSA/blob/master/week3/stack%26queue_155.py)      
-leetcode no.155:min stack，上課所用stack leetcode   
[stack&queue_232](https://github.com/wangshuti/DSA/blob/master/week3/stack%26queue_232.py)   
-leetcode no.232: implement of queue and stack,上課所用queue leetcode      
[課堂筆記](https://github.com/wangshuti/DSA/blob/master/week3/課堂筆記.txt)    
-上課筆記記錄    
[stack_code](https://github.com/wangshuti/DSA/blob/master/week3/stack_code.py)     
-網絡搜尋之stack的基礎code      
[queue_code](https://github.com/wangshuti/DSA/blob/master/week3/queue_code.py)     
-網絡搜尋之queue的基礎code     

## [week4](https://github.com/wangshuti/DSA/tree/master/week4)
### Insertion sort      
Insertion sort是一種簡單直觀的排序演算法。它的工作原理是通過構建有序序列，對於未排序資料，在已排序序列中從後向前掃描，找到相應位置並插入。       
-[補充資料](http://alrightchiu.github.io/SecondRound/comparison-sort-insertion-sortcha-ru-pai-xu-fa.html)     
       
![image](https://github.com/wangshuti/DSA/blob/master/week4/圖解.png)       

[Insertion sort_147](https://github.com/wangshuti/DSA/blob/master/week4/Insertion%20sort_147.py)         
-leetcode no.147: Insertion Sort List, 上課所用Insertion Sort leetcode           
[Insetion sort_code](https://github.com/wangshuti/DSA/blob/master/week4/Insertion%20sort_code.py)         
-Insertion sort 基礎實作code      

## [week5](https://github.com/wangshuti/DSA/tree/master/week5)      
### Quick sort    
Quick Sort是一種「把大問題分成小問題處理」的Divide and Conquer方法，概念如下：         
在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」。        
接著，將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。        
-[補充資料](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)     
           
![image](https://github.com/wangshuti/DSA/blob/master/week5/quick%20sort.png)          
          
[quick sort_code](https://github.com/wangshuti/DSA/blob/master/week5/quick%20sort_code.py)    
-quick sort 基礎實作code，運用額外空間法       
[quick sort_code(2)](https://github.com/wangshuti/DSA/blob/master/week5/quick%20sort_code(2).py)        
-quick sort 方法二：in place法     

### 第一次作業
[流程圖](https://github.com/wangshuti/DSA/blob/master/week5/quick_sort流程圖.jpg)         
-使用draw io畫出來的流程圖，在最後結尾的地方仍存在不妥，正努力解決               
[作業實作](https://nbviewer.jupyter.org/github/wangshuti/DSA/blob/master/week5/HW_quicksort.ipynb)        
-老師要求作業之jupyter notebook格式，因github經常loading不出來，所以放的網頁模式！                         

## week6        
### heap sort         
Binary Heap有兩項基本特徵：       
特徵一：Binary Heap之結構可以視作Complete Binary Tree。         
特徵二：若將位於index(i)之node視為subtree之root，那麼，可將此Binary Heap分為兩類：          
Max Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要大         
Min Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要小       
[補充資料](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)       

## week7
### merge sort
Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。     
Divide：把數列「對半拆解」成兩個小數列。        
Conquer：按照「由小到大」的順序，「合併」小數列。          
[補充資料](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)            

## week8        
### Binary Tree        
         
## week9       
### Binary Serach Tree       

## [week10](https://github.com/wangshuti/DSA/tree/master/week10)                
### Red Black Tree         
         
         
## [week11](https://github.com/wangshuti/DSA/tree/master/week11)         
### Hash Table              
**Hashing**       
Hashing is the process of mapping a search key to a limited range of array indices with the goal of providing direct access to the keys.
The keys are stored in an array called a hash table and a hash function is associated with the table.            
           
**Hash Table**              
哈希表(散列表)，是根據鍵值(key)直接進行訪問的數據結構，即其通過將鍵值映射到表中的某個位置來查找對應的記錄。在此之前，常用的搜尋方法例如線性搜尋法(linear search)或二分搜尋演算法(binary search)都是以比較為基礎的搜尋方法(comparision-based searches)，但以比較為基礎的搜尋演算法其最佳時間複雜度為O(nlogn)，而使用哈希表能提高查詢速度。        

         
**Hash Function**       
哈希表 hash table(key, value)將key通過哈希函數(hash function)轉換為儲存數組的index(H(key) = index)，並將對應的key-value pairs儲存於以index為下標的數組空間中，當使用哈希表進行查詢時，則再次使用哈希函數將key轉換為對應的index，並定位到該空間獲取value。         
              
[**-more information**](https://github.com/wangshuti/DSA/blob/master/HW4/hash_table%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%8C%E6%B5%81%E7%A8%8B%E5%9C%96%EF%BC%8C%E8%AA%AA%E6%98%8E.md)        
           
## [week12](https://github.com/wangshuti/DSA/tree/master/week12)
### Breadth-first search         
>Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.           

广度优先搜索在进一步遍历图中顶点之前，先访问当前顶点的所有邻接结点。           
a .首先选择一个顶点作为起始结点，并将其染成灰色，其余结点为白色。           
b. 将起始结点放入队列中。          
c. 从队列首部选出一个顶点，并找出所有与之邻接的结点，将找到的邻接结点放入队列尾部，将已访问过结点涂成黑色，没访问过的结点是白色。如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现          
d. 按照同样的方法处理队列中的下一个结点。         
         
## [week13](https://github.com/wangshuti/DSA/tree/master/week13)                
### Depth-first search                   
>Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.            

深度优先搜索在搜索过程中访问某个顶点后，需要递归地访问此顶点的所有未访问过的相邻顶点。         
初始条件下所有节点为白色，选择一个作为起始顶点，按照如下步骤遍历：           
a. 选择起始顶点涂成灰色，表示还未访问         
b. 从该顶点的邻接顶点中选择一个，继续这个过程（即再寻找邻接结点的邻接结点），一直深入下去，直到一个顶点没有邻接结点了，涂黑它，表示访问过了        
c. 回溯到这个涂黑顶点的上一层顶点，再找这个上一层顶点的其余邻接结点，继续如上操作，如果所有邻接结点往下都访问过了，就把自己涂黑，再回溯到更上一层。    
d. 上一层继续做如上操作，知道所有顶点都访问过。          
           
### 補充        
**BFS vs. DFS**         
1.在DFS中，使用佇列儲存節點，而在BFS中，使用棧儲存節點。原因就在於二者優先次序的不同。         
2.在搜尋的執行方式上，BFS和DFS也存在差異             
3.所使用的記憶體容量不同             
4.According to tree, they depends on the structure of the search tree             
[-more information](https://github.com/wangshuti/DSA/blob/master/HW5/BFS%26DFS.md)
