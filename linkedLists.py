
class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next  
    
class Linked_list:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node 

    # def length(self):
    #     cur = self.head 
    #     total = 0 
    #     while cur.next != None: 
    #         total += 1 
    #         cur = cur.next 
    #     return total 

    def display(self): 
        if self.head == None:
            print('Linked list is empty')
            return 

        current = self.head
        elems = [] 
        while current != None: 
            elems.append(current.data)
            current = current.next 
        print(elems)
        return 



my_list = Linked_list() 
my_list.insert_at_beginning(23)
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(2)
my_list.display()