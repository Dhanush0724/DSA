
class TreeNode:

    def __init__(self,val=0,right=None,left = None):
        self.val = val
        self.right = right
        self.left  = left

class Solution:


    def diamaterofbinarytree(self,root):

        diameter  = [0]

        self.height(root,diameter)

        return diameter[0]
    
    def height(self,root,diameter):
        if not root:
            return 0
        lh = self.height(root.left,diameter)
        rh = self.height(root.right,diameter)


        diameter[0] = max(diameter[0], lh+rh)

        return 1 + max(lh,rh)

    # Brute Force Method
    # def __init__(self):

    #     self.diameter = 0

    # def calculateHeight(self,root):

    #     if root is None:
    #         return 0
        
    #     left_height = self.calculateHeight(root.left)
    #     right_height = self.calculateHeight(root.right)

    #     self.diameter = max(self.diameter,left_height+right_height)

    #     return 1 + max(left_height,right_height)

    # def diameterofbinaryTree(self,root):

    #     self.calculateHeight(root)

    #     return self.diameter

            





if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.diamaterofbinarytree(root))
    






