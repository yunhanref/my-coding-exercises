#stack
''' FIX THIS
#! Fix adding list elements to the array instead of individual ints.
for i in liste:
    addindex = self.index
    print(f"added to array: {i}")
    self.array[addindex] = i
    self.capacity += 1
'''
class Array():
    def __init__(self,capacity):
        self.capacity = capacity
        self.index = 0
        self.array = [None] * capacity

    def show(self):
        print(self.array)

    def add(self, sayi=int):
        if self.index < self.capacity:
            indeks = self.index
            self.array[indeks] = sayi
            self.index += 1
        else:
            print("full capacity")

    def delete(self, delindex=int):
        print(f"array deleted {delindex} index which is {self.array[delindex]}")
        self.array.pop(delindex)

array = Array(10)
array.add(1)
array.add(2)
array.add(3)
array.add(4)
array.add(5)
array.show()
array.delete(2) #index 2 will be deleted
array.show()




# Stack (pop index 0 always)
class Stack():
    def __init__(self):
        self.stack = []
    def add(self,liste=list):
        for i in liste:
            print(f"added stack element: {i}")
            self.stack.append(i)
    def remove_one(self):
        self.stack.pop() # automatically pop last added index.
    def remove_all(self):
        while len(self.stack) > 0:
            self.stack.pop()
    def show(self):
        print(f"Stack:  {self.stack}")

stack = Stack()
stacklist = [1,2,3,4,5]
stack.add(stacklist)
stack.show()
stack.remove_one()
stack.show()
stack.remove_all()
stack.show()

# Queue
class Queue():
    def __init__(self):
        self.queue = []
        self.first = 0

    def add(self, liste=list):
        for i in liste:
            print(f"added queue val: {i}")
            self.queue.append(i)

    def delete_one(self):
        print(f"popped the first queue element: {self.first}")
        self.queue.pop(self.first)

    def delete_all(self):
        while len(self.queue) > 0:
            print(f"queue popped: {self.queue[self.first]}")
            self.queue.pop(self.first)
        print("queue got deleted completely")

    def show(self):
        if len(self.queue) == 0:
            print("queue empty")
        else:
            print(self.queue)

queue = Queue()
queuelist = [1,2,3,4,5]
queue.add(queuelist)
queue.show()
queue.delete_all()
queue.show()


# Linked List
'''
class Node():
    def __init__(self,value):
        self.value = value
class LinkedList():
    def __init__(self, Node):
        pass
'''