#given a binary tree, check wheather it's a binary search tree or not. 

#first solution: 
    # if tree is a binary search tree, tehn traversing the tree INORDER 
    # should lead to a sorted order of values in the tree. Perform an inorder traversal 
    # and check whether the node values are sorted or not. 


tree = [2,1,3] 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def inorder(self): #will return sorted list if valid BST 
        root = self.val
        if root != None:
            inorder(root.left)
            print(root.val)
            inorder(root.right)

root = TreeNode(2,1,3)
print(root.val, root.left, root.right)
print(root.inorder)