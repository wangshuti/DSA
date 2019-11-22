#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def merge_sort(list):   #分割步驟
        n=len(list)
        left=list[:n//2]   #將list分一半，偶數直接取半，奇數取商
        right=list[n//2:]
        if len(left)>1:     #長度大於1就一直切割，知道切到每個都只有一個為止
            Solution().merge_sort(left)   #採用遞回的方式不停呼叫
        if len(right)>1:
            Solution().merge_sort(right)
        
        i=0    #i=index of left
        j=0    #j=index of right
        l=0    #l=index of list
        while i<len(left) and j<len(right):  #代表left和right互相比較
            if left[i]<=right[j]:    #left的元素小於right的元素時，list[l]就等於left[i]
                list[l]=left[i]
                i+=1                 #輪到left的下一個元素和right來比
            else:                    #再者，right比較小，list[l]就等於right[j]
                list[l]=right[j]
                j+=1                 #輪到right的下一個元素和left來比
            m+=1                     #list的第一個元素決定好了之後，就要加一到第二個元素
        while i<len(left):           #right的元素已經比完並且都放入list裡而left還有
            list[l]=left[i]          #就把剩下的依次放入list裡
            i+=1
            m+=1
        while j<len(right):          #left的元素已經比完並且都放入list裡而right還有
            list[l]=right[j]
            j+=1
            m+=1
        return list
    
    #參考資料：https://medium.com/appworks-school/初學者學演算法-排序法進階-合併排序法-6252651c6f7e

