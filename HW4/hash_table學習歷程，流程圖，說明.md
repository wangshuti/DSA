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

Hash Function有兩種：
-**1.Division Method**：m有限制，但是比較快。         
要把大範圍的|U|對應到較小範圍的{0,1,...,m−1}，最直覺的做法就是利用Modulus(mod)取餘數。
假設Table大小為m，定義Hash Function為：**h(Key)=Key mod m**         
>h(14)=14 mod 8=6 代表「編號14」的物品要放進「第6格」抽屜。
h(23)=23 mod 8=7 代表「編號23」的物品要放進「第7格」抽屜。
h(46)=46 mod 8=6 代表「編號46」的物品要放進「第6格」抽屜。
h(50)=50 mod 8=2 代表「編號50」的物品要放進「第2格」抽屜。

-**2.Multiplication Method**：m沒有限制，但是比較慢。           
由於在實際面對資料時，時常無法預先得知「Key的範圍」以及「在該範圍內Key的分佈情形」，在這個前提下，不需要避開特定m的Multiplication Method可能會比較優秀。        
![image](https://github.com/wangshuti/DSA/blob/master/week11/image/MAD.png)       

-**3.直接定址法**
直接定址法是以数据元素关键字k本身或它的线性函数作为它的哈希地址，即：H（k）=k  或 H（k）=a×k+b          
这种哈希函数简单，并且对于不同的关键字不会产生冲突，但可以看出这是一种较为特殊的哈希函数，实际生活中，关键字的元素很少是连续的。用该方法产生的哈希表会造成空间大量的浪费，因此这种方法适应性并不强。             

-**4.數字分析法**
假设关键字集合中的每个关键字都是由 s 位数字组成 (u1, u2, …, us)，分析关键字集中的全体，并从中提取分布均匀的若干位或它们的组合作为地址。        
>K1=61317602      K2=61326875      K3=62739628      K4=61343634        
K5=62706815      K6=62774638      K7=61381262      K8=61394220           
分析上述8个关键字可知，关键字从左到右的第1、2、3、6位取值比较集中，不宜作为哈希地址，剩余的第4、5、7、8位取值较均匀，可选取其中的两位作为哈希地址。设选取最后两位作为哈希地址，则这8个关键字的哈希地址分别为：2，75，28，34，15，38，62，20。
        
        
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
      




Refernences:      
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html           
https://blog.csdn.net/tanggao1314/article/details/51457585         
