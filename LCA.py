
class TreeNode:

    def __init__(self,val=0,right=None,left = None):
        self.val = val
        self.right = right
        self.left  = left



def findlca(root,x,y):

        if root is None:
            return None
        
        if root.val == x or root.val == y:
            return root
        
        left_lca = findlca(root.left, x,y)
        right_lca = findlca(root.right,x,y)


        if left_lca and right_lca:
             return root
        
        return left_lca if left_lca is not None else right_lca



    

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
print(findlca(root,4,5).val)
    






