class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert_child(self, data):
        if data == self.data:
            return  # node already exists
        
        if data < self.data:
            if self.left:
                self.left.insert_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.insert_child(data)
            else:
                self.right = BSTNode(data)

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        

        return elements
    
    def delete(self,val): 
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else :
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def sum(self):
        left_sum = 0
        right_sum = 0
        if self.left:
            left_sum = self.left.sum()
    
        if self.right:
            right_sum = self.right.sum()

        

        return self.data + left_sum + right_sum


def build_tree(elements):
    print("building tree with these elements", elements)
    root = BSTNode(elements[0])

    for i in range(1, len(elements)):
        root.insert_child(elements[i])

    return root


if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    print("searching 4 :",numbers_tree.search(4))
    
    print("In order Traversal:", numbers_tree.in_order_traversal())

    print("Post order Traversal:", numbers_tree.post_order_traversal())

    print("Pre order Traversal:", numbers_tree.pre_order_traversal())

    numbers_tree.delete(23)
    print("After deleting 23 :",numbers_tree.in_order_traversal())

    print("Sum:",numbers_tree.sum())
    print("Max:",numbers_tree.find_max())
    print("Min:",numbers_tree.find_min())