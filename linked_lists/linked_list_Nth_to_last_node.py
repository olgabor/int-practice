#write a function that takes a node and an integer value n and returns the nth to last node of the linked list 

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


def nth_to_last_node(n, node): 
    pass 

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)