# Traverse through a tree with next methods: 

#tree traversal 
''' Preorder -  visit a root node first, then recursively do a preorder traversal of the left subtree, 
               followed by a recursive  preorder traversal of the right subtree 
    Inorder  -  recursively do an inorder traversal on the left subtree, visit the root node, 
               and finally do a recursive inorder traversal of the right subtree 
    Postorder - recursively do a postorder traversal of the left subtree and the right subtree followed 
                by a visit to the root node''' 


def preorder(tree): 
    if tree: 
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree): 
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree): 
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        
