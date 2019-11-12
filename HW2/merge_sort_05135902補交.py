#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(): 
    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res = res + left + right
        return res

    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        mid = len(lists)//2
        left = Solution().merge_sort(lists[:mid])
        right = Solution().merge_sort(lists[mid:])
        return Solution().merge(left,right)


# In[2]:


merge = Solution().merge_sort([3,2,-4,6,4,2,19])


# In[3]:


print(merge)


# In[ ]:
#參考資料https://medium.com/appworks-school/初學者學演算法-排序法進階-合併排序法-6252651c6f7e
#參考資料http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html




