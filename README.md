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
