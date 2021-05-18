#Binary Search Tree: 
    #Left sub-tree of a node have values LOWER than or equal to the node 
    #Right sub-tree of a node have values BIGGER than the node 
#main usage is searching 
#        10 
#     /      \ 
#   8         12  - leaf node (parent)
#  /         /    \ 
# 5        11      15 - (child leaf)


class Node:
    #initilizes the init method 
    def __init__(self, value): # takes the value of the Node 
        self.left = None 
        self.right = None 
        self.data = value #whatever value we create the node with 
    
    
    def insert(root,node): #root of the tree and Node 
        if (root is None): 
            root = node 
            return 
        if(root.data < node.data):
            if(root.right is None): 
                root.right = node 
            else: 
                insert(root.right, node)
        else:
            if(root.left is None):
                root.left = node 
            else:
                insert(root.left, node)


    def preorder(node):
        if (node is not None):
            print(node.data)
            preorder(node.left)
            preorder(node.right)

#         5
#     /      \ 
#    3        7
#   / \      / \
#  2   4    6   8 
tree = Node(5) #creating the root 
#         5
#     /      \ 
#   None     None 

tree.insert(Node(3))
#         5
#     /      \ 
#   3        None 
tree.insert(Node(2))
#         5
#     /      \ 
#   3        None 
#  /
# 2
tree.insert(Node(4))
#         5
#     /      \ 
#   3        None 
#  /  \
# 2    4 
tree.insert(Node(7))
#         5
#     /      \ 
#   3        7
#  /  \
# 2    4 
tree.insert(Node(6))
#         5
#     /      \ 
#   3         7
#  /  \      /
# 2    4    6
tree.insert(Node(8))
#         5
#     /      \ 
#   3         7
#  /  \      /  \
# 2    4    6    8 

tree.preorder()