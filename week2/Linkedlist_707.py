Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyLinkedList(object):



    def __init__(self):

        """

        Initialize your data structure here.

        """

        self.val = None

        self.next = None



    def get(self, index):

        """

        Get the value of the index-th node in the linked list. If the index is invalid, return -1.

        :type index: int

        :rtype: int

        """

        if self.val == None:

            return -1

        if index == 0:

            return self.val

        p = self.next

        i = 1

        while p != None:

            if i == index:

                return p.val

            p = p.next

            i += 1

        return -1



    def addAtHead(self, val):

        """

        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

        :type val: int

        :rtype: None

        """

        if self.val == None:

            self.val = val

            return

        temp = self.val

        self.val = val

        tempnode = self.next

        self.next = MyLinkedList()

        self.next.val = temp

        self.next.next = tempnode

        return



    def addAtTail(self, val):

        """

        Append a node of value val to the last element of the linked list.

        :type val: int

        :rtype: None

        """

        if self.val == None:

            self.val = val

            return

        p = self

        while p.next != None:

            p = p.next

        p.next = MyLinkedList()

        p.next.val = val

        return







    def addAtIndex(self, index, val):

        """

        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.

        :type index: int

        :type val: int

        :rtype: None

        """

        i = 0

        p = self

        pre = p

        if index <= 0:

            self.addAtHead(val)

            return

        while i < index:

            i += 1

            pre = p

            if p != None and p.val != None:

                p = p.next

            else:

                return

        pre.next = MyLinkedList()

        pre.next.val = val

        pre.next.next = p

        return 



    def deleteAtIndex(self, index):

        """

        Delete the index-th node in the linked list, if the index is valid.

        :type index: int

        :rtype: None

        """

        i = 0

        p = self

        if index < 0:

            return

        if index == 0:

            if self.val == None:

                return

            if self.next == None:

                self = None

                return

            self.val = self.next.val

            self.next = self.next.next

        pre = p

        while i < index:

            i += 1

            pre = p

            if pre == None:

                return

            p = p.next

        if p != None:

            pre.next = p.next

        else:

            pre.next = None

        return
