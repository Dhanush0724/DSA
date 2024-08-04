class TreeNode:

    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

# def BalancedTree(root):
#     if not root :
#         return True
#     left_depth = getHeight(root.left)
#     right_depth = getHeight(root.right)
    
#     if abs(left_depth - right_depth) <= 1 and BalancedTree(root.left) and BalancedTree(root.right):
#         return True 
    
#     return False

# def getHeight(root):

#     if not root:
#         return 0
    
#     leftheight = getHeight(root.left)
#     rightheight = getHeight(root.right)

#     return max(leftheight,rightheight) + 1

def isbalanced(root):

    return dfsheight(root) != -1

def dfsheight(root):

    if not root :
        return 0 
    
    left_height = dfsheight(root.left)

    if left_height == -1:
        return -1
    
    right_height = dfsheight(root.right)

    if right_height == -1:
        return -1
    
    if abs(left_height - right_height ) > 1:
        return -1
    
    return max(left_height, right_height) + 1

def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        node = queue.pop(0)
        if values[index] != -1:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] != -1:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index +=1
    
    return root

values = [1,3,2,5,4,-1,-1,7,6]
root = build_tree(values)
# print(BalancedTree(root))
if isbalanced(root):
    print("Trure")
else :
    print("Fgasle")