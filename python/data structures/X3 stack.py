#Son giren ilk çıkar (LIFO) mantığıyla çalışır. Sadece en üste eleman eklenir ve en üstten alınır.

class Yigin:
    def __init__(self):
        self.yigin_kutusu = []

    def ustten_ekle(self, yeni_eleman):
        self.yigin_kutusu.append(yeni_eleman)

    def ustten_cikar(self):
        if len(self.yigin_kutusu) > 0:
            return self.yigin_kutusu.pop() # Listenin en sonundaki (en üstteki) elemanı sil ve ver
        else:
            return "Yığın tamamen boş!"




class Stack():
    def __init__(self):
        self.stack = []
    def add_to_stack(self, stack_elemani=list):
        for i in stack_elemani:
            print(f"adding {i}")
            self.stack.append(i)
    def remove_last_from_stack(self):
        length = len(self.stack)
        while length > 0:
            print(f"deleting {length}th element of stack")
            self.stack.pop()
            length -= 1
    def show_stack(self):
        print(self.stack)



myStack = Stack()
mylist = [1,2,3,4,5]
myStack.add_to_stack(mylist)
myStack.show_stack()
myStack.remove_last_from_stack()
myStack.show_stack()