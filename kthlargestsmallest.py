
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.val  = val
        self.left = left
        self.right = right
# #### BRUTE FORCE APPROACH
# def kthindex(root,key,stack):
#     if not root:
#         return
#     kthindex(root.left,key,stack)
#     stack.append(root.val)
#     kthindex(root.right,key,stack)
#     return 
# def findkth(root,key):
#     stack = []
#     kthindex(root,key,stack)
#     klargest = stack[len(stack) - key]
#     ksmallest = stack[key-1]
#     return (ksmallest,klargest)

def inorder(root,counter,key,smallest):

    if not root or counter[0] > key:
        return
    
    inorder(root.left,counter,key,smallest)

    counter[0] +=1

    if counter[0] == key:
        smallest[0] = root.val
        return
    


    inorder(root.right,counter,key,smallest)

def reverse_inorder(root,counter,key,largest):

    if not root or counter[0] >=key:
        return
    
    reverse_inorder(root.right,counter,key,largest)

    counter[0] +=1

    if counter[0] == key:
        largest[0] = root.val
        return
    
    reverse_inorder(root.left,counter,key,largest)


def findkth(root,key):

    smallest = [float('inf')]
    largest = [float('-inf')]

    counter = [0]

    inorder(root,counter,key,smallest)

    counter[0] = 0
    reverse_inorder(root,counter,key,largest)

    return (smallest , largest)

def printorder(root):
   
   if root is None:
      return
   
   printorder(root.left)

   print(root.val,end=" ")

   printorder(root.right)



if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    

    printorder(root)
    print()
    key = 3
    result = findkth(root,key)
    print(result)


