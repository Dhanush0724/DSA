
class Node:
    def __init__(self,val):

        self.data = val
        self.left = None
        self.right = None

class Solution:

    def findmaxpathsum(self,root,maxi):

        if root is None:
            return 0 
         
        leftmaxpath = max(0,self.findmaxpathsum(root.left,maxi))
        rightmaxpath = max(0,self.findmaxpathsum(root.right,maxi))

        maxi[0] = max(maxi[0], leftmaxpath+rightmaxpath)

        return max(leftmaxpath,rightmaxpath) + root.data
    
    def maxpathsum(self,root):

        maxi = [float('-inf')]

        self.findmaxpathsum(root,maxi)

        return maxi[0]
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()

# Finding and printing the maximum path sum
maxPathSum = solution.maxpathsum(root)
print("Maximum Path Sum:", maxPathSum)
