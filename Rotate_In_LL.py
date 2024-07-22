class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
def rotate(head,k):
        if head == None or head.next == None:
            return head
        
        for i in range(k):
            temp = head
            while temp.next.next != None:
                temp = temp.next
            end = temp.next
            temp.next = None
            end.next = head
            head = end
        return head
    
def printll(head):
        ll = ''
        itr = head
        while itr:
            ll+=str(itr.data) +'->'
            itr = itr.next
        ll +='None'
        return ll
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

ro = rotate(head,2)
print(printll(ro))
