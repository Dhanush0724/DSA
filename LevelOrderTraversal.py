from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        
        q = deque([root])

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans

    @staticmethod
    def printList(lst):
        for num in lst:
            print(num, end=' ')
        print()

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
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    # Printing the level order traversal result
    for level in result:
        Solution.printList(level)
