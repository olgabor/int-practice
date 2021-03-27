# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
 
# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:

    def __init__(self):
        self.items = []
        self.min_items = [float('inf')]

    def push(self, val):
        self.items.append(val)
        #append the new value to min_stak only if it's smaller than last value in min_stack
        if val <= self.min_items[-1]:  
            self.min_items.append(val)

    def pop(self):
        d = self.items.pop()
        # remove the value from min_stack only if is == to self.items.pop()
        if d == self.min_items[-1]:
            self.min_items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def getMin(self):
        return self.min_items[-1]
        

# Your MinStack object will be instantiated and called as such:
# Example 1
obj = MinStack()
obj.push(1)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)


# Example 2
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
obj1 = MinStack()
obj1.push(-2)
obj1.push(0)
obj1.push(-3)
param1_4 = obj1.getMin() 
obj1.pop()
param1_3 = obj1.top()
param1_5 = obj1.getMin() 
print(param1_3, param1_5)
