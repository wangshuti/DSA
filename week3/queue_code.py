Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Queue(object):
	#陣列
	def _init_(self):
		self._list = []

		
>>> def enqueue(self,item):
	#新增元素
	return self._list.append(item)

>>> def dequeue(self):
	#從頭部刪除一個元素
	return self._list.pop(0)

>>> def is_empty(self):
	#判斷是否為空
	return self._list == []

>>> def size(self):
	#返回陣列的大小
	return len(self._list)

>>> 
