
class Node:
    def __init__(self,val):

        self.data = val
        self.left = None
        self.right = None

class Solution:

    def isidentical(self,node1,node2):

        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None:
            return False
        
        return (node1.data == node2.data and self.isidentical(node1.left,node2.left) and self.isidentical(node1.right,node2.right))
    
    
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

solution = Solution()

if solution.isidentical(root1, root2):
    print("The binary trees are identical.")
else:
    print("The binary trees are not identical.")
