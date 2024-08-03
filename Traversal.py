class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def preorder(root, arr):
    if not root:
        return
    arr.append(root.data)  
    preorder(root.left, arr)  
    preorder(root.right, arr)  

def preOrder(root):
    arr = []
    preorder(root, arr)
    return arr

def inorder(root, arr):
    if not root:
        return
    
    inorder(root.left, arr) 
    arr.append(root.data)   
    inorder(root.right, arr)  

def inOrder(root):
    arr = []
    inorder(root, arr)
    return arr


def postorder(root, arr):
    if not root:
        return
    
    postorder(root.left, arr) 
       
    postorder(root.right, arr)  
    arr.append(root.data)

def postOrder(root):
    arr = []
    postorder(root, arr)
    return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    

    
    result = preOrder(root)
    result1 = inOrder(root)
    result2 = postOrder(root)
    
    print("Preorder Traversal:", end=" ")
    for val in result:
        print(val, end=" ")
    print()

    print("inorder Traversal:", end=" ")
    for val in result1:
        print(val, end=" ")
    print()

    print("postorder Traversal:", end=" ")
    for val in result2:
        print(val, end=" ")
    print()

