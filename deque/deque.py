class Deque: 

    def __init__(self): 
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)
    
    def removeFront(self): 
        return self.items.pop(0) 

    def removeRear(self): 
        return self.items.pop() 
    
    def size(self): 
        return len(self.items) 
    
    def isEmpty(self): 
        return self.items == []
    
d = Deque()
print(d.size())
print(d.isEmpty())
print(d.addFront('Hello'))
print(d.addRear('World'))

print(d.removeFront() + ' ' + d.removeRear()) 
