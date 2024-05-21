class Stack :
    def __init__(self) :
        self.stack = []
#use to add elements
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else :
            return False
# used to look on top of the stack
    def peek(self):
        return self.stack[-1]
    

    def remove(self):
        if len(self.stack) <=0:
            return("NO elements in the stack")
        else :
            return self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def view(self):
        return self.stack.copy()
        

    
s = Stack()
s.add(1)
s.add(2)
s.add(3)
print(s.view())
s.remove()
print(s.peek())
print(s.size())
print(s.is_empty())


    

