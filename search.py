
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.val  = val
        self.left = left
        self.right = right

def search(root,key):

    while root is not None and root.val != key:

        root = root.left if key < root.val else root.right

    return root

def printorder(root):
   
   if root is None:
      return
   
   printorder(root.left)

   print(root.val,end=" ")

   printorder(root.right)



if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)

    printorder(root)
    print()
    key = 6
    result = search(root,key)
    if result is not None:
        print(f"values {key} found in BST ")
    else:
        print(f"values {key} not found in BST")


