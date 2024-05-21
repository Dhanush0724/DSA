from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
    
    def addstart(self,item):
        self.queue.appendleft(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def view(self):
        return list(self.queue)  # Convert to list to view elements

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.view())  # Output: [1, 2, 3]
print(q.peek())  # Output: 1
print(q.dequeue())  # Output: 1
print(q.size())  # Output: 2
print(q.is_empty())  # Output: False
q.addstart(0)
print(q.view())