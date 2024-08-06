
from collections import deque
class TreeNode:

    def __init__(self,val=0,right=None,left = None):
        self.val = val
        self.right = right
        self.left  = left

class Solution:


    def zigzag(self,root):
        result = []

        if not root:
            return result
        
        nodesQueue = deque()

        nodesQueue.append(root)

        lefttoright = True

        while nodesQueue:
            
            size = len(nodesQueue)

            row = [0]*size

        for i in range(size):

            node = nodesQueue.popleft()

            index = i if lefttoright else (size-i-1)

            row[index] = node.data

            if node.left:
                nodesQueue.append(node.left)
                
            if node.right:
                nodesQueue.append(node.right)

        lefttoright = not lefttoright

        result.append(row)
    

        return result

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.zigzag(root))
    






