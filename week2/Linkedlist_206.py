
>>> def reverseList(self, head):
    prev = None
        
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
        
    return prev
