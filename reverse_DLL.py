class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def convert_arr_to_dll(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    itr = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        itr.next = new_node
        new_node.prev = itr
        itr = new_node

    return head

def reverse_dll(head):
    if head is None or head.next is None:
        return head
    
    temp = None
    current = head

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    
    # After the loop, temp will be pointing to the new head's previous node.
    if temp is not None:
        head = temp.prev

    return head

def print_dll(head):
    itr = head
    dll = ''
    while itr:
        dll += '<--' + str(itr.data) + '-->'
        itr = itr.next
    print(dll)

arr = [12, 5, 6, 8, 7]
head = convert_arr_to_dll(arr)
print("Original DLL:")
print_dll(head)
head = reverse_dll(head)
print("Reversed DLL:")
print_dll(head)
