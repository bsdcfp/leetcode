import os
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
    def size(self):
        return len(self.__items)

class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__items.pop(0)

    def size(self):
        return len(self.__items)

if __name__ == '__main__':
    s = Stack()

    s.push(12)
    s.push(23)
    s.push(89)
    print s.size()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()

    q = Queue()
    q.enqueue(12)
    q.enqueue(23)
    q.enqueue(89)
    print q.size()
    print q.dequeue()    
    print q.dequeue()
