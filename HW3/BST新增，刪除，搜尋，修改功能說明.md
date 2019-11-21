# Binary search tree       
## 新增insert           
默認一開始傳進來的值為root，根據左邊的子節點比父節點小，右邊的子節點比父節點大的原則         
注意：相等時看是取小於等於還是大於等於                
在插入時，要一層一層的往下比較          
具體流程：          
1.若一開始是空树，则将傳進來的值s作为根节点(root)插入，否则：           
2.若s小于等於binary search tree的根节点之值，则把s所指节点插入到左子树中，否则：           
3.把s所指节点插入到右子树中。（新插入节点总是叶子节点）         

## 刪除delete        
注意：採取最小變動的原則！！！                  
1.刪除23                     
若刪去值p為最下層子節點，則它無子樹。刪除不會破壞整個樹的結構，修改雙親節點的指針即可                 
![image](https://github.com/wangshuti/DSA/blob/master/image/d1.JPG)                 
2.刪除41                  
若p節點只有左子樹（PL）或右子樹（PR)，此時只要令PL或PR直接成為其母樹的節點的子樹就可           
![image](https://github.com/wangshuti/DSA/blob/master/image/d2.JPG)                         
3.刪除12         
若p左子樹與右子樹均不為空，在刪p之後，要保持最小變動，則較為複雜               
此時就需要找p的Successor和Predecessor            
補充：               
Successor(S)找的是「right subtree中Key最小的node」；            
Predecessor(P)找的是「left subtree中Key最大的node」；                
因此Successor和Predecessor必定不會同時也有兩個child                                 
![image](https://github.com/wangshuti/DSA/blob/master/image/d3.JPG)         
現在想要刪除12，S為23，P為4。所以在這種情況下，用23或4將12替換即可不改變樹原本的結構。        
但因要求更動最少，因此選擇23.         

## 查詢search                          
會有兩種情況：                  
1.搜尋的值key找到匹配的值，搜尋成功                        
2.搜尋的值key最後傳到NULL，則搜尋失敗                 
範例：                   
若現在要從BST中搜尋基紐隊長，便以基紐隊長（627）進入BST。 進入BST後，便把用來移動的Current指向root           
![image](https://github.com/wangshuti/DSA/blob/master/image/s1.png)            
接著將KEY(627)和比克(root)的戰鬥力(513)比較，結果是基紐隊長戰勝，因此，基紐隊長如果在BST裡面，應該會長在比克的right subtree裡面，於是便將Current往比克的right child(達爾)移動              
![image](https://github.com/wangshuti/DSA/blob/master/image/s2.png)       
將Current移動到達爾之後，再將KEY(627)與達爾的戰鬥力(524)比較，結果仍然是基紐隊長大，因此步驟同上，繼續將Current往達爾的right child(弗力札)移動    
![image](https://github.com/wangshuti/DSA/blob/master/image/s3.png)            
將Current移動到弗力札之後，再將KEY(627)與弗力札的戰鬥力(709)比較，結果是弗力札略勝，於是便往弗力札的left child尋找基紐隊長         
![image](https://github.com/wangshuti/DSA/blob/master/image/s4.png)                  
此時，Current的Key(627)與傳送進Search()的KEY(627)相同，便確認Current即為基紐隊長，於是跳出while迴圈，並傳回Current。        
宣告搜尋成功。        

## 修改modify      
此處修改要求全部替換，且可以更換root。需保證原來的樹高要大於等於修改後的樹高！        
我自己的理解則是：刪去需要修改的值，而新增修改後的值！ 
範例：          
![image](https://github.com/wangshuti/DSA/blob/master/image/modify.jpg)        
           
參考資料：          
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html              
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html         
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html 
