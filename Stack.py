class Stack(object):
    def __init__(self): #creating stack
        self.mystack = []
    
    def isEmpty(self): #Checking whether the stack is empty or not
        return self.mystack == []
    
    def push(self,item):  #addition of items in the stack
        self.mystack.append(item)
    
    def pop(self): #removing items from stack
        return self.mystack.pop()
    
    def peek(self):  #To peek the top of stack
        return self.mystack[len(self.mystack)-1]
    
    def view(self):
        return self.mystack

    def size(self):
        return len(self.mystack)

s = Stack()

# print(s.isEmpty())
# s.push(1)
# s.push('two')
# print(s.pop())
# s.push('gibrish')
# print(s.peek())
# print(s.size())
# print(s.isEmpty())
for i in range(11):
    s.push(i)
print(s.view())