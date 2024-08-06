class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        def leftBoundary(node):
            boundary = []
            while node:
                if node.left or node.right:
                    boundary.append(node.val)
                node = node.left if node.left else node.right
            return boundary
        
        def rightBoundary(node):
            boundary = []
            while node:
                if node.left or node.right:
                    boundary.append(node.val)
                node = node.right if node.right else node.left
            return boundary[::-1]
        
        def leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return leaves(node.left) + leaves(node.right)
        
        boundary = []
        if root:
            boundary.append(root.val)
            boundary += leftBoundary(root.left)
            boundary += leaves(root.left)
            boundary += leaves(root.right)
            boundary += rightBoundary(root.right)
        
        return boundary

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.boundaryTraversal(root))
