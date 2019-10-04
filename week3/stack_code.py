
>>> class Stack(object):
	def _init_(self):
		self._list=[]
#創立棧
		
>>> def push(self,item):
	self._list.append(item)
#新增一個到棧頂
	
>>> def pop(self):
	return self._list.pop()
#彈出

>>> def peek(self):
	if self._list:
		return self._list[-1]
	else:
		return None
#返回
	
>>> def is_empty(self):
	return self._list == []
#判斷是否為空

>>> def size(self):
	return len(self._list)
#返回元素個數
