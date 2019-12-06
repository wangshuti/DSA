# Hashing
Hashing is the process of mapping a search key to a limited range of array indices with the goal of providing direct access to the keys.     
The keys are stored in an array called a hash table and a hash function is associated with the table.      
             
## Hash Table
要了解hash table，首先要熟悉dictionary的概念       
>### Dictionary
>>Dictionary是以「鍵值-資料對」(Key-Value pair)來描述資料的抽象資料形態(Abstract Data Type)。      
>>例子：       
>>-電話簿裡的Dictionary即是將「姓名」視為Key，「電話號碼」視為Value。       
>>-學校學籍系統的Dictionary將「學號」視為Key，「學生資料」(如姓名、修課記錄)視為Value。<br>        
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/DIC.JPG)
     
而hash table是 Dictionary 類別中雜湊表的一種實作。            
哈希表(散列表)，是根據鍵值(key)直接進行訪問的數據結構，即其通過將鍵值映射到表中的某個位置來查找對應的記錄。在此之前，常用的搜尋方法例如線性搜尋法(linear search)或二分搜尋演算法(binary search)都是以比較為基礎的搜尋方法(comparision-based searches)，但以比較為基礎的搜尋演算法其最佳時間複雜度為O(nlogn)，而使用哈希表能提高查詢速度。     
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/hash%20table.JPG)
         
## Hash Function
哈希表 hash table(key, value)將key通過哈希函數(hash function)轉換為儲存數組的index(H(key) = index)，並將對應的key-value pairs儲存於以index為下標的數組空間中，當使用哈希表進行查詢時，則再次使用哈希函數將key轉換為對應的index，並定位到該空間獲取value。       
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/hash%20function.JPG)           
A “perfect” hash function will map every key to a different table entry, resulting in no collisions. But this is seldom achieved except in cases like our collection of products in which the keys are within a small range or when the keys are known beforehand. Instead, we try to design a good hash function that will distribute the keys across the range of hash table indices as evenly as possible.        
>1.計算應該簡單以便產生快速結果         
2.結果index不能是隨機的。當哈希函數多次應用於同一key時，它必須始終返回相同的index。           
3.如果key包含多個部分，則每個部分都應參與計算所得的index。        
4.表的大小應為素數，尤其是在使用模數時操作員。這樣可以產生更好的分佈並減少碰撞減少共享相同除數的鍵的數量。<br>        

**常見的Hash Function有兩種：**                     
-**1.Division Method**：m有限制，但是比較快。         
要把大範圍的|U|對應到較小範圍的{0,1,...,m−1}，最直覺的做法就是利用Modulus(mod)取餘數。
假設Table大小為m，定義Hash Function為：`h(Key)=Key mod m`        
>h(14)=14 mod 8=6 代表「編號14」的物品要放進「第6格」抽屜。          
h(23)=23 mod 8=7 代表「編號23」的物品要放進「第7格」抽屜。            
h(46)=46 mod 8=6 代表「編號46」的物品要放進「第6格」抽屜。              
h(50)=50 mod 8=2 代表「編號50」的物品要放進「第2格」抽屜。             
              
-**2.Multiplication Method**：m沒有限制，但是比較慢。           
由於在實際面對資料時，時常無法預先得知「Key的範圍」以及「在該範圍內Key的分佈情形」，在這個前提下，不需要避開特定m的Multiplication Method可能會比較優秀。        
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/MAD.png)       
              
**補充**            
-**3.直接定址法**          
直接定址法是以数据元素关键字k本身或它的线性函数作为它的哈希地址，即：H（k）=k  或 H（k）=a×k+b                
这种哈希函数简单，并且对于不同的关键字不会产生冲突，但可以看出这是一种较为特殊的哈希函数，实际生活中，关键字的元素很少是连续的。用该方法产生的哈希表会造成空间大量的浪费，因此这种方法适应性并不强。                  
            
-**4.數字分析法**        
假设关键字集合中的每个关键字都是由 s 位数字组成 (u1, u2, …, us)，分析关键字集中的全体，并从中提取分布均匀的若干位或它们的组合作为地址。           
>K1=61317602      K2=61326875      K3=62739628      K4=61343634        
K5=62706815      K6=62774638      K7=61381262      K8=61394220           
分析上述8个关键字可知，关键字从左到右的第1、2、3、6位取值比较集中，不宜作为哈希地址，剩余的第4、5、7、8位取值较均匀，可选取其中的两位作为哈希地址。设选取最后两位作为哈希地址，则这8个关键字的哈希地址分别为：2，75，28，34，15，38，62，20。         
           
-**5.折疊法**          
  将关键字分割成若干部分，然后取它们的叠加和为哈希地址。两种叠加处理的方法：移位叠加:将分 割后的几部分低位对齐相加；边界叠加:从一端沿分割界来回折叠，然后对齐相加。                    
  所谓折叠法是将关键字分割成位数相同的几部分（最后一部分的位数可以不同），然后取这几部分的叠加和（舍去进位），这方法称为折叠法。这种方法适用于关键字位数较多，而且关键字中每一位上数字分布大致均匀的情况。               
  折叠法中数位折叠又分为移位叠加和边界叠加两种方法，移位叠加是将分割后是每一部分的最低位对齐，然后相加；边界叠加是从一端向另一端沿分割界来回折叠，然后对齐相加。              
>当哈希表长为1000时，关键字key=110108331119891，允许的地址空间为三位十进制数，则这两种叠加情况如图：
       移位叠加                                 边界叠加                         
       8 9 1                                     8 9 1            
       1 1 9                                     9 1 1              
       3 3 1                                     3 3 1              
       1 0 8                                     8 0 1                
    +  1 1 0                                   + 1 1 0 <br>                                                  
  (1) 5 5 9                                  (3)0 4 4                         
 用移位叠加得到的哈希地址是559，而用边界叠加所得到的哈希地址是44。如果关键字不是数值而是字符串，则可先转化为数。转化的办法可以用ASCⅡ字符或字符的次序值。                   
            
-**6.平方取中法**                  
  这是一种常用的哈希函数构造方法。这个方法是先取关键字的平方，然后根据可使用空间的大小，选取平方数是中间几位为哈希地址。               
  哈希函数 H(key)=“key2的中间几位”因为这种方法的原理是通过取平方扩大差别，平方值的中间几位和这个数的每一位都相关，则对不同的关键字得到的哈希函数值不易产生冲突，由此产生的哈希地址也较为均匀。            
         
-**7.減去法**         
减去法是数据的键值减去一个特定的数值以求得数据存储的位置。            
>例7，公司有一百个员工，而员工的编号介于1001到1100，减去法就是员工编号减去1000后即为数据的位置。编号1001员工的数据在数据中的第一笔。编号1002员工的数据在数据中的第二笔…依次类推。从而获得有关员工的所有信息，因为编号1000以前并没有数据，所有员工编号都从1001开始编号。             
            
-**8.基數轉換法**         
  将十进制数X看作其他进制，比如十三进制，再按照十三进制数转换成十进制数，提取其中若干为作为X的哈希值。一般取大于原来基数的数作为转换的基数，并且两个基数应该是互素的。               
>例Hash(80127429)=(80127429)13=8*137+0*136+1*135+2*134+7*133+4*132+2*131+9=(502432641)10如果取中间三位作为哈希值，得Hash（80127429）=432      

還有許多其他的hash function方法，請參考[HERE](https://blog.csdn.net/tanggao1314/article/details/51457585)           
Hash Function設計不易，很難完美，有可能會把兩個不同的 key 指到同一個value，這就是所謂的 collision。       
       
## Collision
>若以Division Method實作Hash Function，定義h(Key)=Keymodm，Table大小為m=6，目前要處理的資料之Key有67,26,50,33,16,71，那麼各個Key將被對應到的index如下:        
>>h(67)=67 mod 6=1     
h(26)=26 mod 6=2        
h(50)=50 mod 6=2       
h(33)=33 mod 6=3       
h(16)=16 mod 6=4         
h(71)=71 mod 6=5         
>「item26」與「item50」經過Hash Function後，同時想要將資料存進Table[2]，這就是Collision。                 
                  
**常見的解決collision的方法：           
1.開放地址法**            
这种方法也称再散列法，其基本思想是：当关键字key的哈希地址p=H（key）出现冲突时，以p为基础，产生另一个哈希地址p1，如果p1仍然冲突，再以p为基础，产生另一个哈希地址p2，…，直到找出一个不冲突的哈希地址pi ，将相应元素存入其中。
>这种方法有一个通用的再散列函数形式：`Hi=（H（key）+di）% m i=1，2，…，n`               
其中H（key）为哈希函数，m 为表长，di称为增量序列。增量序列的取值方式不同，相应的再散列方式也不同。         
主要有以下三种：       
>>**线性探测再散列**         
`dii=1，2，3，…，m-1`         
这种方法的特点是：冲突发生时，顺序查看表中下一单元，直到找出一个空单元或查遍全表。            

>>**二次探测再散列**          
`di=12，-12，22，-22，…，k2，-k2 ( k<=m/2 )`           
这种方法的特点是：冲突发生时，在表的左右进行跳跃式探测，比较灵活。          

>>**伪随机探测再散列**          
`di=伪随机数序列。`          
具体实现时，应建立一个伪随机数发生器，（如i=(i+p) % m），并给定一个随机数做起点。             

**2.再哈希法**
这种方法是同时构造多个不同的哈希函数：         
` Hi=RH1（key） i=1，2，…，k`          
当哈希地址Hi=RH1（key）发生冲突时，再计算Hi=RH2（key）……，直到冲突不再产生。这种方法不易产生聚集，但增加了计算时间。         
           
**3.链地址法**
这种方法的基本思想是将所有哈希地址为i的元素构成一个称为同义词链的单链表，并将单链表的头指针存在哈希表的第i个单元中，因而查找、插入和删除主要在同义词链中进行。链地址法适用于经常进行插入和删除的情况。           
             
**4.建立公共溢出区**            
这种方法的基本思想是：将哈希表分为基本表和溢出表两部分，凡是和基本表发生冲突的元素，一律填入溢出表。           
               
## 流程圖     
### Add
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/add.png)
### Contain
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/contain.png)
### Remove
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/remove.png)
## Code and Learning
```Python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        if not self.contains(key):
            [key_str, key_int, idx] = self.genMD5(key)
            #print(key_int)
            #print(idx)
            if self.data[idx] == None:               #如果下標為index的數組空間為空
                self.data[idx] = ListNode(key_int)   #則將儲存hash_value值的節點直接存於該空間
            else:                                    #如果下標為index的數組空間已經有節點
                node = self.data[idx] 
                while node.next != None:             #不斷走訪                  
                    node = node.next                 #將儲存hash_value值的節點接在最後一個節點後
                node.next = ListNode(key_int)

    def remove(self, key):       
        if self.contains(key):              #如果contains函數執行結果為True，即該key仍然存在
            [key_str, key_int, idx] = self.genMD5(key)
            if self.data[idx].val == key_int:           #如果linked list頭結點的值即為該key之hash_value
                self.data[idx] = self.data[idx].next    #原來頭結點的後一個節點即為新的頭結點
            else:
                p = self.data[idx]           #儲存比對節點的前一個節點
                node = self.data[idx].next   #真正的比對從頭結點的後一個節點開始
                while node != None:
                    if node.val == key_int:  #如果該節點的值等於key_int
                        p.next = node.next   #則將該節點前一個節點指向該節點的後一個節點
                        return
                    else:
                        p = node             #否則，需後移一位
                        node = node.next

    def contains(self, key):        
        [key_str, key_int, idx] = self.genMD5(key)      #用MD5編碼處理後
        if self.data[idx] == None:       #如果沒有index，回傳錯誤
            return False
        else:
            node = self.data[idx]        #讓節點=index
            while node != None:          #如果此時節點存在
                if node.val == key_int:
                    return True          #回傳的確存在 
                else:                    #否則繼續走訪
                    node = node.next
        return False

    def genMD5(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))

        key_str = h.hexdigest()           #用MD5加碼
        key_int = int(h.hexdigest(), 16)  #提出其中數字的部分
        idx = key_int % self.capacity     #用取餘數法得到作為index

        return [key_str, key_int, idx]

    def show(self):
        for n in range(self.capacity):
            print("%d:" % n)
            node = self.data[n]
            while node != None:
                print(node.val)
                node = node.next
```               
Refernences:      
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html           
https://blog.csdn.net/tanggao1314/article/details/51457585         
https://zhuanlan.zhihu.com/p/29520044
