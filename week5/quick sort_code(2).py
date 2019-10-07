>>> def quick_sort2(list, left, right):
    if left >= right:
        return list
    key = list[left]
    left_pivot = left
    right_pivot = right
    while left_pivot < right_pivot:
        while left_pivot < right_pivot and list[right_pivot] >= key: 
            right_pivot = right_pivot - 1
        while left_pivot < right_pivot and list[left_pivot] <= key: 
            left_pivot = left_pivot + 1
        if left_pivot < right_pivot:
            list[left_pivot], list[right_pivot] = list[right_pivot], list[left_pivot]
    list[left], list[left_pivot] = list[left_pivot], list[left] 
    quick_sort2(list, left, left_pivot - 1
    quick_sort2(list, right_pivot + 1, right)
    return list

>>> def quick_sort(list):
    return quick_sort2(list, 0, len(list)-1)

>>> mylist = [20, 9, 100, 0, 55, 3, 11]
>>> print ("result：", quick_sort(mylist))
result： [0, 3, 9, 11, 20, 55, 100]
>>> 
