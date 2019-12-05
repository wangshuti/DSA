from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        if not self.contains(key):
            [key_str, key_int, idx] = self.genMD5(key)
            #print(key_int)
            #print(idx)
            if self.data[idx] == None:
                self.data[idx] = ListNode(key_int)
            else:
                node = self.data[idx]
                while node.next != None:
                    node = node.next
                node.next = ListNode(key_int)

    def remove(self, key):       
        if self.contains(key):
            [key_str, key_int, idx] = self.genMD5(key)
            if self.data[idx].val == key_int:
                self.data[idx] = self.data[idx].next
            else:
                p = self.data[idx]
                node = self.data[idx].next
                while node != None:
                    if node.val == key_int:
                        p.next = node.next
                        return
                    else:
                        p = node
                        node = node.next

    def contains(self, key):        
        [key_str, key_int, idx] = self.genMD5(key)
        if self.data[idx] == None:
            return False
        else:
            node = self.data[idx]
            while node != None:
                if node.val == key_int:
                    return True
                else:
                    node = node.next
        return False

    def genMD5(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))

        key_str = h.hexdigest()
        key_int = int(h.hexdigest(), 16)
        idx = key_int % self.capacity

        return [key_str, key_int, idx]

    def show(self):
        for n in range(self.capacity):
            print("%d:" % n)
            node = self.data[n]
            while node != None:
                print(node.val)
                node = node.next
