class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# # Brute Force MEhtod
# def detect_loop(head):

#     temp = head

#     node_set = set()

#     while temp is not None:

#         if temp in node_set:
#             return True
        
#         node_set.add(temp)
#         temp = temp.next
#     return False

#### Optimal approach 

def detect_loop(head):
    slow = head
    fast  = head
    

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


### counting the loop length
def counting(head):
    slow = head
    fast  = head
    
    
    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            fast = fast.next

            while slow!=fast:
                fast = fast.next
                length+=1
        
            return length
    
    return 0
            
        
    
    
    

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    
    # Check if there is a loop
    # in the linked list
    if detect_loop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    print(counting(head))