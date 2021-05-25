#Implement Singly lonked list

#1st example 
# class Node():
#     #keep the list of all Nodes 
#     nodes = []

#     def __init__(self, value):
#         self.value = value
#         self.nextnode = None 
#         self.__class__.nodes.append(value)

# #'1'->'2'->'3'-> None 
# a = Node(1) 
# b = Node(2)
# c = Node(3)

# a.nextnode = b
# b.nextnode = c 

# #print Nodes 
# current_node = a 
# while True: 
#     print(current_node.value, '->', end=' ')
#     if current_node.nextnode == None: 
#         print('None')
#         break 
#     current_node = current_node.nextnode

# # or print the Nodes one by one: 
# print(a.value, a.nextnode.value, b.nextnode.value )

# #print list of all Nodes 
# print(Node.nodes)

##########################################################
# 2nd example 
#class to create single Node 
class LinkedListNode(): 
    def __init__(self, value, next_node=None):
        self.value = value 
        self.next_node = next_node 


class LinkedList:
    def __init__(self, head=None): 
        self.head = head

    def insert(self, value): 
        node = LinkedListNode(value)

        # if linked list has no element adding new Node to head 
        if self.head is None:
            self.head = node                   # inserting the element 
            return 

        currentNode = self.head 
        while True:
            if currentNode.next_node is None: # checking if this is a tail 
                currentNode.next_node = node
                break
            currentNode = currentNode.next_node


    def insert_by_index(self,index, element ):

        current_node = self.head              # start from head 

        if index == 0:                        # if index is 0 replace the head with new node 
            new_node = LinkedListNode(element, next_node=current_node)
            self.head = new_node
            return 

        for i in range(index - 1): 
            prev_node = current_node 
            current_node = prev_node.next_node

        new_node = LinkedListNode(element, next_node = current_node)
        prev_node.next_node = new_node


    def get_element_by_index(self, index):
        node = self.head 
        prev_node = self.head
        
        for i in range(index): 
            prev_node = node 
            node = node.next_node
   
        return prev_node.value


    def print_linked_list(self):
        currentNode = self.head

        while currentNode is not None: 
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.next_node 
        print('None')


    #delete node by value 
    def delete_node(self, number): 
        node = self.head
        if node is None: 
            return

        if node.value == number:
            self.head = node.next_node
            node = None
            return

        while (node.value != number):        # traverse untill next node matches the value 
            prev_node = node                 # save the previous node 
            node = node.next_node

        prev_node.next_node = node.next_node 
        node = None

    
    def has_cycle(self): 
        if self.head == None: 
            return 
        
        marker1 = self.head
        marker2 = self.head.next_node 

        while marker1 != marker2: 

            if marker1 is None or marker2.next_node is None:
                return False   
            
            marker1 = marker1.next_node 
            marker2 = marker2.next_node

        return True 

    # length of the list 
    def get_length(self): 
        node = self.head 
        i = 1 
        if node is None: 
            return 0
        
        while node.next_node: 
            node = node.next_node
            i+= 1 
        return i 

linked_list = LinkedList()
# linked_list.print_linked_list()
linked_list.insert(3)
# linked_list.print_linked_list()
linked_list.insert(2)
linked_list.insert(2)
# linked_list.print_linked_list()
linked_list.insert(8)
linked_list.insert(8)
# linked_list.print_linked_list()
linked_list.insert_by_index(0, 900)
linked_list.print_linked_list()
linked_list.insert_by_index(4, 88000)
linked_list.print_linked_list()
linked_list.insert_by_index(3, 100)
linked_list.print_linked_list()
linked_list.delete_node(2)
linked_list.print_linked_list()
linked_list.delete_node(900)
linked_list.print_linked_list()
linked_list.get_element_by_index(4)

print(linked_list.get_length())