# given a singly linked list, write a funciton that takes in the first node in the singly linked list 
# and returns a boolean indicating if the linked list contains a 'cycle' 

#Cycle - when next point points to the previous node in the list 

def cycle_check(node): 
    marker1 = node 
    marker2 = node 

    while marker2 != None and marker2.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode 

        if marker1 == marker2:
            return True 

    return False 

#implement the linked lists to test the solution 
class Node(): 

    def __init__(self, value): 
        self.value = value 
        self.nextnode = None 
        self.prevnode = None 

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

#############
class TestCycleCheck(object):
    
    def test(self,sol):
        print(sol(a) == True)
        print(sol(x) == False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests
t = TestCycleCheck()
t.test(cycle_check)