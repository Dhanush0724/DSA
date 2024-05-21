
class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def addtop(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    
    def size(self):
        return len(self.queue)
    
    def remove(self):
        if len(self.queue) >0:
            return self.queue.pop()
        else :
            return ("No elements in the quweue!!!")
        
    def enqueue(self,data):
        self.queue.append(data)

    def is_empty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)
    
    def view(self):
        return list(self.queue)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.view())
print(q.size())
print(q.is_empty())
        
