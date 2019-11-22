# Binary search tree       
## 新增insert           
默認一開始傳進來的值為root，根據左邊的子節點比父節點小，右邊的子節點比父節點大的原則         
注意：相等時看是取小於等於還是大於等於                
在插入時，要一層一層的往下比較          
具體流程：          
1.若一開始是空树，则将傳進來的值s作为根节点(root)插入，否则：           
2.若s小于等於binary search tree的根节点之值，则把s所指节点插入到左子树中，否则：           
3.把s所指节点插入到右子树中。（新插入节点总是叶子节点）         
```Python           
def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val)     #如果為空就變成root
        elif val == root.val:
            nn = TreeNode(val)
            nn.left = root.left      #等於放左邊
            root.left = nn
        elif val < root.val:
            root.left = self.insert(root.left, val)      #小於也放左邊，往左走
        elif val > root.val:
            root.right = self.insert(root.right, val)    #大於放右邊，往右走
        return root
```

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
```Python
 def findMin(self, root):          #找尋最小值的函數，delete時需要用到
        if root.left:
            return self.findMin(root.left)
        else:
            return root
            
    def delete(self, root, val):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if root == None:
            return
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left and root.right:                     #想刪除的值有兩個子節點，及左右都有
                temp = self.findMin(root.right)              #因此找到右子樹中最小的值，與想要刪除的值進行替換
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            elif root.right == None and root.left == None:        #沒有子節點，直接刪除
                root = None
            elif root.right == None:                   #只有左節點，直接連parent
                root = self.delete(root.left,val)
            elif root.left == None:                    #只有右節點，直接連parent
                root = root.right
        return root
``` 

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
``` Python
def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None:         #如果樹為空，就直接回傳
            return root
        if root.val == target:     #如果想找的值為root，回傳
            return root
        elif target < root.val:     
            return self.search(root.left, target)      #如果想找的值比root小，則往左走
        elif target > root.val:
            return self.search(root.right, target)     #如果想找的值比root大，則往右走
```

## 修改modify      
此處修改要求全部替換，且可以更換root。需保證原來的樹高要大於等於修改後的樹高！        
我自己的理解則是：刪去需要修改的值，而新增修改後的值！ 
範例：          
![image](https://github.com/wangshuti/DSA/blob/master/image/modify.jpg)        
```Python
   def count(self, root, val):     #計算是否想要修改的數有重複的函數
        if root == None:
            return 0
        if root.val == val:
            return 1 + self.count(root.left, val)
        if val < root.val:
            return self.count(root.left, val)
        if val > root.val:
            return self.count(root.right, val)

    def getDepth(self, root):                    #計算樹的深度
        depth = 0
        if root == None:
            return depth
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        return max(left, right) + 1

    def helper(self, A, s, e):                         #定義如果需變更節點的函數
        root = None
        if s < e:
            mid = (s + e) >> 1
            root = TreeNode(A[mid])                      #選擇中間值為節點，使樹兩邊平均
            root.left = self.helper(A, s, mid - 1)
            root.right = self.helper(A, mid + 1, e)
        elif s == e:
            root = TreeNode(A[s])
        return root

    def sortList(self, root):
        rtn = []
        if root == None:
            return rtn
        a = self.sortList(root.left)
        b = self.sortList(root.right)
        return a + [root.val] + b


    def modify(self, root, val, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        cnt = self.count(root, val)     #想修改的值有多少個
        oldDepth = self.getDepth(root)  #原樹高

        node = self.delete(root, val)   #刪除想要修改的值
        while node and cnt:
            self.insert(node, new_val)  #insert新的值
            cnt -= 1
        newDepth = self.getDepth(node)
        if newDepth > oldDepth:               #如果新樹比舊樹高，調整
            lst = self.sortList(node)
            if lst is None or len(lst) == 0:
                return None
            res = self.helper(lst, 0, len(lst) - 1)
            return res
        else:                                 #否則直接回傳                    
            return node
``` 
參考資料：          
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html              
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html         
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html 
