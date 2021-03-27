# Write a function to delete a node in a singly-linked list. 
# You will not be given access to the head of the list, 
# instead you will be given access to the node to be deleted directly.

# It is guaranteed that the node to be deleted is not a tail node in the list.
class Node():

    nodes = [] 

    def __init__(self, x): 

        self.__class__.nodes.append(x)
        self.value = x 
        self.next = None 

a = Node(4)
b = Node(5)
c = Node(1)
d = Node(9)
a.next = b
b.next= c
c.next = d

print(Node.nodes)

def delete_node(node): 
    node.val = node.next.value 
    node.next = node.next.next 
  
