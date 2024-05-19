class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinked:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_begin(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            print("No items to delete")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr

    def delete_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.prev.next = None
        else:
            print("No items to delete")

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Give correct index man!!!")
        
        if index == 0:
            self.insert_begin(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        dll = ''
        while itr:
            dll += "<--" + str(itr.data) + "-->"
            itr = itr.next
        print(dll)

if __name__ == '__main__':
    D = DoublyLinked()
    D.insert_begin(2)
    D.insert_begin(4)
    D.delete_begin()
    D.insert_end(8)
    D.delete_end()
    D.insert_end(8)
    D.insert_end(16)
    D.print()
    D.insert_at(1, 4)
    D.insert_at(2, 5)
    D.print()
    print(D.get_length())
