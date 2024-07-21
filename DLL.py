class Node:
    def __init__(self,data=None,prev=None,next=None) :
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begin(self,data):
        new_node = Node(data,None,self.head)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else :
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr
        
    def delete_begin(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            self.head = self.head.next
            self.head.prev = None
        else :
            print("There is no Node to deltet")

    def delete_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.prev.next = None



    def print(self):
        itr = self.head
        dll = ''
        while itr:
            dll+= "<--" +str(itr.data) + "-->"
            itr = itr.next
        print(dll)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_end(4)
    dll.insert_end(6)
    dll.insert_begin(2)
    dll.delete_begin()
    dll.delete_end()
    dll.print()