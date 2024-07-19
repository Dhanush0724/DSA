
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next and slow:

        fast = fast.next.next

        slow = slow.next
    
    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

middle = find_middle(head)


print(middle.data)