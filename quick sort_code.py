Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def quick_sort(list):
	min = []
	max = []
	keylist = []

	
>>> if len(list) <= 1:
	return list
SyntaxError: 'return' outside function
>>> def quick_sort(list):
	min = []
	max = []
	keylist = []

	
>>> def quick_sort(list):
	min = []
	max = []
	keylist = []
	
SyntaxError: invalid syntax
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
