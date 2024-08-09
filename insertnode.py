
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.val  = val
        self.left = left
        self.right = right

def insert(root,key):

    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left =  insert(root.left,key)
    else :
        root.right = insert(root.right,key)
    
    return root

def printorder(root):
   
   if root is None:
      return
   
   printorder(root.left)

   print(root.val,end=" ")

   printorder(root.right)



if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    

    printorder(root)
    print()
    key = 5
    result = insert(root,key)
    if result is not None:
        print(f"values {key} inserted ")
    else:
        print(f"values {key} not inserted")
    printorder(root)
    print()


