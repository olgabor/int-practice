#Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.


#steps 
    # stack reverses the order while queue doesn't 
    # sequence of elements pushed on stack comes back in reversed order when poped
    # two stacks chained together will return elemetns in the same order, since reversed order reversed again is original order 

    # use in-stack that we fill when the element is enqueued and dequeue operation takes alements from out-stack
    # if the out-stack element is empty - we pop all elements from the in-stack and pysh them onto out-stack 

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x) 
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outstack: 
            while self.instack: 
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()
    

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outstack: 
            while self.instack: 
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.instack and not self.outstack 

#input 
# ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]        

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)