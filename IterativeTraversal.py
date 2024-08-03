from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):

        preorder = []

        if root is None:
            return preorder
        
        st = []
        st.append(root)

        while st:

            root = st.pop()

            preorder.append(root.val)

            if root.right:
                st.append(root.right)
            
            if root.left:
                st.append(root.left)
            
        return preorder
        
    
    

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.preorder(root)

    print("Pre Order Iterative Traversal of Tree:")

    # Printing the level order traversal result
    for val in result:
        print(val, end=' ')
