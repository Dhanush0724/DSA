class TreeNode:

    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def MaxHeight(root):
    if root is None:
        return 0
    left_depth = MaxHeight(root.left)
    right_depth = MaxHeight(root.right)
    return max(left_depth,right_depth) + 1


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

values = [1,2,5,-1,-1,4,6,5]
root = build_tree(values)
print(MaxHeight(root))