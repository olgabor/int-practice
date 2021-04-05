#Implement Singly lonked list

#1st example 
class Node():
    #keep the list of all Nodes 
    nodes = []

    def __init__(self, value):
        self.value = value
        self.nextnode = None 
        self.__class__.nodes.append(value)

#'1'->'2'->'3'-> None 
a = Node(1) 
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c 

#print Nodes 
current_node = a 
while True: 
    print(current_node.value, '->', end=' ')
    if current_node.nextnode == None: 
        print('None')
        break 
    current_node = current_node.nextnode

# or print the Nodes one by one: 
print(a.value, a.nextnode.value, b.nextnode.value )

#print list of all Nodes 
print(Node.nodes)

##########################################################
# 2nd example 
#class to create single Node 
class LinkedListNode(): 
    def __init__(self, value, next_node=None):
        self.value = value 
        self.next_node = next_node 

#class 
class LinkedList:
    def __init__(self, head=None): 
        self.head = head

    def insert(self, value): 
        node = LinkedListNode(value)

        # checking is there is no Nodes 
        if self.head is None:
            self.head = node                   # inserting the element 
            return

        currentNode = self.head 
        while True:
            if currentNode.next_node is None: # checking if this is a tail 
                currentNode.next_node = node
                break
            currentNode = currentNode.next_node
    
    def delete_node(self, value): 
        pass 


    def print_linked_list(self):
        currentNode = self.head

        while currentNode is not None: 
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.next_node 
        print('None')
        
linked_list = LinkedList()
linked_list.print_linked_list()
linked_list.insert(3)
linked_list.print_linked_list()
linked_list.insert(2)
linked_list.print_linked_list()
linked_list.insert(8)
linked_list.print_linked_list()