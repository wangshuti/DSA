Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ListNode:

  def __init__(self, data): 

    # store data

    self.data = data

    # store the reference (next item)

    self.next = None

    return

    

node1 = ListNode(15)

#建立一個帶有15的資料的節點了

    

class SingleLinkedList:

  def __init__(self): 

    self.head = None

    self.tail = None

    return



#在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：

#若list本身還沒有任何節點，則head以及tail都會變成新的結點

#若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。

    

def add_list_item(self, item):

  # make sure item is a proper node  

  if not isinstance(item, ListNode):

    item = ListNode(item)

    

  if self.head is None:

    self.head = item

  else:

    self.tail.next = item

   

  self.tail = item

  return

#其中比較需要注意的是，在取得item之後，要檢查item是否是一個結點，若不是的話則使用ListNode(item)建立一個帶有item資料的節點。 

  



list1 = SingleLinkedList()

list1.add_list_item(node1)

list1.add_list_item(12)
