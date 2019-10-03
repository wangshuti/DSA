Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Stack(object):
	def _init_(self):
		self._list=[]

		
>>> def push(self,item):
	self._list.append(item)

	
>>> def pop(self):
	return self._list.pop()

>>> def peek(self):
	if self._list:
		return self._list[-1]
	else:
		return None

	
>>> def is_empty(self):
	return self._list == []

>>> def size(self):
	return len(self._list)

>>> if _name_ == '_main_':
	s=Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())

	
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    if _name_ == '_main_':
NameError: name '_name_' is not defined
>>> 
