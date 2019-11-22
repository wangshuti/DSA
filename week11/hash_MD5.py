from Crypto.Hash import MD5
h = MD5.new()
h.update("i am pecu".encode("utf-8"))
print(h.hexdigest())
x = int(h.hexdigest(),16)
print(x%5)
