#Represent a tree through list 

def BinaryTree(r): #r = root
    return [r,[],[]]

def instertRight(root, newBranch): 
    t = root.pop(1)

    if len(t) > 1: 
        root.insert(1, [newBranch, t, []])
    else: 
        root.insert(1, [newBranch, [], []])
    
    return root 

def instertLeft(root, newBranch): 
    t = root.pop(2)

    if len(t) > 1: 
        root.insert(2, [newBranch, t, []])
    else: 
        root.insert(2, [newBranch, [], []])
    
    return root 

def getRootVal(root): 
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
print(instertLeft(r, 4))
print(instertRight(r, 5))
print(instertLeft(r, 6))
print(instertRight(r, 7))
