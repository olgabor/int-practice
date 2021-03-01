# stack implementation 

class Stack(object): 

    def __init__ (self): 
        self.items = []

    def isEmpty(self): #returns True/False wheather the stack is empty or not 
        return self.items == [] 

    def push(self, item): #adds new item to the top of the stack 
        self.items.append(item)
    
    def pop(self): #removes the top item from the stack 
        return self.items.pop()
    
    def peek(self): #returns the top item from stack 
        return self.items[len(self.items) -1]

    def size(self): #returns the number of items in stack 
        return len(self.items)
    
s = Stack()

print(s.isEmpty())

s.push(1)
s.push('two')
print(s.peek())
print(s.size())

print(s.isEmpty())
s.pop()
print(s.size())
s.pop()
print(s.isEmpty())