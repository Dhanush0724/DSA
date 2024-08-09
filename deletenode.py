
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.val  = val
        self.left = left
        self.right = right

def delete(root,key):

    if root is None:
        return None
    
    if key < root.val:
        root.left =  delete(root.left,key)
    elif key > root.val :
        root.right = delete(root.right,key)
    else :
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        min_larger_node = getmin(root.right)
        root.val = min_larger_node.val
        root.right = delete(root.right, root.val)
    
    return root

def getmin(node):
    while node.left is not None:
        node = node.left
    
    return node


def printorder(root):
   
   if root is None:
      return
   
   printorder(root.left)

   print(root.val,end=" ")

   printorder(root.right)



if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    

    printorder(root)
    print()
    key = 3
    result = delete(root,key)
    if result is not None:
        print(f"values {key} deletef ")
    else:
        print(f"values {key} not deleted")
    printorder(root)
    print()


