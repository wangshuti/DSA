>>> def quick_sort(list):
	small=[]
	big=[]
	keylist=[]
	if len(list) <= 1:
		return list
	else:
		key = list[0]
		for i in list:
			if i < key:
				small.append(i)
			elif i > key:
				big.append(i)
			else:
				keylist.append(i)
	small = quick_sort(small)
	big = quick_sort(big)
	return small+keylist+big

>>> mylist = [3,24,13,2,4,56,74,54,15]
>>> quick_sort(mylist)
[2, 3, 4, 13, 15, 24, 54, 56, 74]
>>> 
