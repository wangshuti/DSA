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
            if self.data[idx] == None:               #如果下標為index的數組空間為空
                self.data[idx] = ListNode(key_int)   #則將儲存hash_value值的節點直接存於該空間
            else:                                    #如果下標為index的數組空間已經有節點
                node = self.data[idx] 
                while node.next != None:             #不斷走訪                  
                    node = node.next                 #將儲存hash_value值的節點接在最後一個節點後
                node.next = ListNode(key_int)

    def remove(self, key):       
        if self.contains(key):              #如果contains函數執行結果為True，即該key仍然存在
            [key_str, key_int, idx] = self.genMD5(key)
            if self.data[idx].val == key_int:           #如果linked list頭結點的值即為該key之hash_value
                self.data[idx] = self.data[idx].next    #原來頭結點的後一個節點即為新的頭結點
            else:
                p = self.data[idx]           #儲存比對節點的前一個節點
                node = self.data[idx].next   #真正的比對從頭結點的後一個節點開始
                while node != None:
                    if node.val == key_int:  #如果該節點的值等於key_int
                        p.next = node.next   #則將該節點前一個節點指向該節點的後一個節點
                        return
                    else:
                        p = node             #否則，需後移一位
                        node = node.next

    def contains(self, key):        
        [key_str, key_int, idx] = self.genMD5(key)      #用MD5編碼處理後
        if self.data[idx] == None:       #如果沒有index，回傳錯誤
            return False
        else:
            node = self.data[idx]        #讓節點=index
            while node != None:          #如果此時節點存在
                if node.val == key_int:
                    return True          #回傳的確存在 
                else:                    #否則繼續走訪
                    node = node.next
        return False

    def genMD5(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))

        key_str = h.hexdigest()           #用MD5加碼
        key_int = int(h.hexdigest(), 16)  #提出其中數字的部分
        idx = key_int % self.capacity     #用取餘數法得到作為index

        return [key_str, key_int, idx]

    def show(self):
        for n in range(self.capacity):
            print("%d:" % n)
            node = self.data[n]
            while node != None:
                print(node.val)
                node = node.next

#Refernences:      
#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html           
#https://blog.csdn.net/tanggao1314/article/details/51457585         
#https://zhuanlan.zhihu.com/p/29520044               
#僅參考概念，程式碼原創
