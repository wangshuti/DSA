>>> list = [20,9,100,0,55,3,11]

>>> def insertion_sort(list):
	for i in range(1,len(list)):
		tmp = list[i]
		j = i-1
		while j >= 0 and tmp < list[j]:
			list[j+1] = list[j]
			j = j-1
		list[j+1] = tmp
		print("pass",i,":",list)

		
>>> insertion_sort(list)
pass 1 : [9, 20, 100, 0, 55, 3, 11]
pass 2 : [9, 20, 100, 0, 55, 3, 11]
pass 3 : [0, 9, 20, 100, 55, 3, 11]
pass 4 : [0, 9, 20, 55, 100, 3, 11]
pass 5 : [0, 3, 9, 20, 55, 100, 11]
pass 6 : [0, 3, 9, 11, 20, 55, 100]
>>> 
