class Queue: 

    def __init__(self): 
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self): 
        return self.items.pop() 
    
    def size(self): 
        return len(self.items) 
    
    def isEmpty(self): 
        return self.items == []


q= Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(2)
q.enqueue(1)
q.enqueue(9)
print(q.dequeue())