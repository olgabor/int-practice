# write a function to reverse a linked list in place 
# the function will take in the head of the list as input and return the new head of the list 

class Node(object):
    nodes = []
    def __init__(self,value):
        self.__class__.nodes.append(value)
        self.value = value
        self.nextnode = None

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


print(Node.nodes)
print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

##############################
def reverse(node): 
    
    current = node
    previous = None 
    nextnode = None 
   
    while current: 
        nextnode = current.nextnode #remember the current node 
        current.nextnode = previous #assign current node to None 
        previous, current = current, nextnode #swap the values 

    return previous 

print(reverse(a))

print (b.nextnode.value)
print (c.nextnode.value)
print (d.nextnode.value)
print(Node.nodes)