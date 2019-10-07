>>> def quick_sort(list):
	min=[]
	max=[]
	keylist=[]
	if len(list) <= 1:
		return list
	else:
		key = list[0]
		for i in list:
			if i < key:
				min.append(i)
			elif i > key:
				max.append(i)
			else:
				keylist.append(i)
	min = quick_sort(min)
	max = quick_sort(max)
	return min+keylist+max

>>> mylist = [3,24,13,2,4,56,74,54,15]
>>> quick_sort(mylist)
[2, 3, 4, 13, 15, 24, 54, 56, 74]
>>> 
