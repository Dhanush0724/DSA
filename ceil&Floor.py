
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.val  = val
        self.left = left
        self.right = right

def ceil(root,key):

    ceil = -1

    while root:

        if root.val == key:
            ceil = root.val
            return ceil
        
        if key > root.val:
            root = root.right
        else :
            ceil = root.val
            root = root.left
    
    return ceil

def floor(root,key):

    floor = -1

    while root:

        if root.val == key:
            floor = root.val
            return floor
        
        if key > root.val:
            floor = root.val
            root = root.right
        else :
            
            root = root.left
    
    return floor

def printorder(root):
   
   if root is None:
      return
   
   printorder(root.left)

   print(root.val,end=" ")

   printorder(root.right)

   


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(13)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(4)
    root.left.right = TreeNode(6)
    root.left.right.right = TreeNode(9)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(14)

    printorder(root)
    print()
    key = 8
    print(ceil(root,key))
    print(floor(root,key))


