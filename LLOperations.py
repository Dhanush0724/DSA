class Node:

    def __init__(self, data= None, next = None) :
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is  None:
            self.head = Node(data,None)
            return
        
        else :
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)



    def delete_at_end(self):
        if self.head is None:
            print("Node is empty")
        
        if self.head.next is None:
            self.head = None
            return
        
        else :
            itr = self.head
            while itr.next.next:
                itr = itr.next
            itr.next = None


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return print(count)

    def search_element(self,target):
        itr = self.head

        while itr:
            if itr.data == target:
                return print(True)
            itr = itr.next
        return print(False)
                


    def print(self):
        if self.head is None:
            print("linked list is empty")

        itr = self.head
        llstr = ""
        while itr :
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
if __name__ == "__main__":
    li = Linkedlist()
    li.insert_at_end(2)
    li.insert_at_end(4)
    li.insert_at_end(6)
    li.print()
    li.delete_at_end()
    li.print()
    li.get_length()
    li.search_element(4)
    

