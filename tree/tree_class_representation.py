
class BinaryTree(object): 

    def __init__(self, root_obj): 
        self.key = root_obj 
        self.left_child = None 
        self.right_child = None 

    def insert_left(self, new_node):
        # if no childs are present 
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        #if we have a child we are adding a new node and pushing existing child down the tree  
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child 
            self.left_child = t 


    def insert_right(self, new_node):
         # if no childs are present 
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        #if we have a child we are adding a new node and pushing existing child down the tree  
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t 

    def get_right_child(self): 
        return self.right_child

    def get_left_child(self): 
        return self.left_child 
    
    def set_root_val(self, obj):
        self.key = obj 

    def get_root_val(self): 
        return self.key 

    def print_tree(self, traversal_type):
        if traversal_type == "preorder": 
            return self.preorder_print(root, "")
        if traversal_type == "inorder": 
            return self.inorder_print(root, "")
        if traversal_type == "postorder": 
            return self.postorder_print(root, "")
        else: 
            pritn('Traversal type ' + str(traversal_type) + 'is not supported.')
            return 

    def preorder_print(self, start, traversal): 
        """ Root -> Left -> Right """
        if start: 
            traversal += (str(start.key) + "-")
            traversal = self.preorder_print(start.left_child, traversal)
            traversal = self.preorder_print(start.right_child, traversal)
        return traversal 
    

    def inorder_print(self, start, traversal): 
        """ Left -> Root -> Right """
        if start:
            traversal = self.inorder_print(start.left_child, traversal)
            traversal += (str(start.key) + "->")
            traversal = self.inorder_print(start.right_child, traversal)
        return traversal 

    def postorder_print(self, start, traversal): 
        """  Left -> Right  -> Root"""
        if start:
            traversal = self.postorder_print(start.left_child, traversal)
            traversal = self.postorder_print(start.right_child, traversal)
            traversal += (str(start.key) + "->")
        return traversal
            
#              1 
#            /    \
#          2       3 
#        /   \    /  \ 
#       4     5  6    7 

root = BinaryTree(1)
root.left_child = BinaryTree(2)
root.right_child = BinaryTree(3)
root.left_child.left_child = BinaryTree(4)
root.left_child.right_child = BinaryTree(5)
root.right_child.left_child = BinaryTree(6)
root.right_child.right_child= BinaryTree(7)

# 1 - 2 - 4 - 5 - 3 - 6 - 7 - 
print(root.print_tree("preorder"))
# 4 - 2 - 5 - 1 - 6 - 3 - 7 - 
print(root.print_tree("inorder"))
# 4 - 2 - 5 - 6 - 3 - 7 - 1  
print(root.print_tree("postorder"))



#tree traversal methods 
def preorder(tree): 
    if tree: 
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree): 
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree): 
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())
    
# print(preorder(r))
# print('---------') 
# print(postorder(r))
# print('---------') 
# print(inorder(r))

# print(preorder(root))
# r = BinaryTree('a')
# print(r.get_root_val())
# r.insert_left('b')
# r.insert_right('c')
# print(r.get_left_child().get_root_val())
