#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
class Solution():
    def adjust(self, heap, k, n):
        root = k
        tmp = heap[root]
        child = 2 * root

        while child <= n:
            if child < n and heap[child] < heap[child + 1]:
                child = child + 1
            if tmp > heap[child]:
                break
            else:
                heap[math.floor(child / 2)] = heap[child]
                child = child * 2

        heap[math.floor(child / 2)] = tmp

    def heap_sort(self, heap):
        heap.insert(0, 0);
        n = len(heap) - 1;

        i = math.floor(n / 2)

        for x in range(i, 0, -1):
            Solution().adjust(heap, x, n)

        i = n - 1

        for y in range(i, 0, -1):
            temp = heap[1]
            heap[1] = heap[y + 1]
            heap[y + 1] = temp

            Solution().adjust(heap, 1, y)
        return heap[1:]


# In[2]:


heap = Solution().heap_sort([3,2,-4,6,4,2,19])


# In[3]:


print(heap)


# In[ ]:

#無參考程式資料，自創


