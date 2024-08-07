
class TreeNode:

    def __init__(self,val=0,right=None,left = None):
        self.val = val
        self.right = right
        self.left  = left

# ######  Brute Force Method
# def inorder(root,count):
#     if root is  None:
#         return 0 
#     count[0] +=1
#     inorder(root.left,count)
#     inorder(root.right,count)

# def countNodes(root):
#     if root is None:
#         return 0
#     count = [0]
#     inorder(root,count)
#     return count[0]

## Optimal Approach

def calculatenodes(root):
    if not root :
        return 0 
    
    lh = findheightleft(root)
    rh = findheightright(root)

    if lh ==  rh:
        return (1 << lh) - 1
    
    return 1 + calculatenodes(root.left) + calculatenodes(root.right)
    
def findheightleft(node):

    height = 0 
    while node:
        height+=1
        node = node.left
    return height

def findheightright(node):

    height = 0 
    while node:
        height+=1
        node = node.right
    return height

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(calculatenodes(root))
    






