import math


class solution():
    def adjust(self,heap, k, n):
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

    def heapsort(self,heap):
        heap.insert(0,0);
        n = len(heap)-1;

        i = math.floor(n / 2)

        for x in range(i, 0, -1):
            solution().adjust(heap, x, n)

        i = n - 1

        for y in range(i, 0, -1):
            temp = heap[1]
            heap[1] = heap[y + 1]
            heap[y + 1] = temp

            solution().adjust(heap, 1, y)
        
        del heap[0]
        
        return heap



heap = solution().heapsort([3,2,-4,6,4,2,19])

print( heap )


#參考資料：http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
#程式碼原創

