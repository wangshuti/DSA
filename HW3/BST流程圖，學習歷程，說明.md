# BST的特性：
## 1.為二元樹，即每個節點最多有兩個子節點     
## 2.永遠遵循“左小右大“原則       
          
## 學習歷程       
我先完成了關於BST新增，刪除，搜尋，修改功能說明的作業。在網上搜尋資料來幫助自己理解。             
然後再進行手繪流程圖。各個功能的流程圖確定無誤後才開始撰寫程式。          
在撰寫程式之前按老師說的回顧了一下之前的linkedlist和binary tree的程式碼。在這兩個基礎上程式碼好寫很多。         
雖然沒有一下子就完成程式碼，但大的框架出來，後面進行debug發現許多是小細節的問題。程式的邏輯沒有問題。             
          
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
