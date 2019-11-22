# BST的特性：
## 1.為二元樹，即每個節點最多有兩個子節點     
## 2.永遠遵循“左小右大“原則       
          
## 學習歷程       
從上次作業得到經驗是對概念的理解很重要！不要一上來就試著寫程式碼。         
因此大部分時間是花在理解三個功能上，尤其是delete的部分         
我先在網上搜尋資料來幫助自己理解。             
然後再進行手繪流程圖。各個功能的流程圖確定無誤後才開始撰寫程式。(如下圖）                    
在撰寫程式之前按老師說的回顧了一下之前的linkedlist和binary tree的程式碼。在這兩個基礎上程式碼好寫很多。         
雖然沒有一下子就完成程式碼，但大的框架出來，後面進行debug發現許多是小細節的問題。程式的邏輯沒有問題。
但程式碼仍有未完善的部分：modify要求樹高為最小可能，這點仍在探索！         
——[linkedlist basic code](https://github.com/wangshuti/DSA/blob/master/week2/Linkedlist_note.py)
          
## 新增功能
![image](https://github.com/wangshuti/DSA/blob/master/image/insert手.jpg)          

## 查詢功能
![image](https://github.com/wangshuti/DSA/blob/master/image/搜尋.jpg)         
            
查詢功能與新增功能都很好理解          
這次作業的難點是刪除和修改        

## 刪除功能
分為三種情況討論：           
1.所刪除的值沒有子節點        
2.所刪除的值只有一個左或右子節點        
3.所刪除的值有兩個子節點        
![image](https://github.com/wangshuti/DSA/blob/master/image/刪除.jpg)        
           
## 修改功能           
網絡上查不到資料，自行理解！          
我的理解：先搜尋到想要修改的值，執行定義好的delete函數，再insert想改後的值！         
![image](https://github.com/wangshuti/DSA/blob/master/image/modify.jpg)      
```Python
def count(self, root, val):
        if root == None:
            return 0
        if root.val == val:
            return 1 + self.count(root.left, val)
        if val < root.val:
            return self.count(root.left, val)
        if val > root.val:
            return self.count(root.right, val)

    def modify(self, root, val, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        cnt = self.count(root, val)
        node = self.delete(root, val)
        while node and cnt:
            self.insert(node, new_val)
            cnt -= 1
        return node
```       
        
參考資料（僅參考概念）       
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html        
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html        
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html          
