class deque(object):
    def __init__(self):
        self.list = []
    
    def IsEmpty(self):
        return self.list == []
    
    def pushrear(self,item):
        self.list.insert(0,item)
    
    def pushFront(self,item):
        self.list.append(item)
    
    def popfront(self):
        return self.list.pop()
    
    def poprear(self):
        return self.list.pop(0)
    
    def peek(self):
        return self.list
    
    def size(self):
        return len(self.list)

d = deque()
d.pushFront(1)
d.pushFront(2)
d.pushrear(3)
d.pushrear(4)
print(d.peek())
