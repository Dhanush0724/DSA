class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class circular_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head!= None:
            temp = self.head
            while(temp.next!=self.head):
                temp = temp.next
            temp.next = new_node
        else :
            new_node.next = new_node
        self.head = new_node
        return self.head

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    
if __name__ == "__main__":
    C = circular_linked_list()
    C.insert_at_end(10)
    C.print()
